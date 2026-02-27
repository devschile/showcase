#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<EOF
Usage: $0 GITHUB_URL

Given a GitHub repo URL (https://github.com/owner/repo),
this script fetches the repository README, extracts a short summary,
and creates a project Markdown file under `_projects/`.

Example:
  $0 https://github.com/owner/repo

Notes:
- Requires `curl`, `sed`, `awk` (available on macOS/Linux).
- If the repo's default branch cannot be discovered, the script will try `main` then `master`.
EOF
}

if [[ ${#} -lt 1 ]]; then
  usage
  exit 1
fi

GITHUB_URL="$1"

# Normalize URL and extract owner/repo
clean=$(echo "$GITHUB_URL" | sed -E 's#https?://([^/]+/)?github.com/##' | sed -E 's#git$##' | sed -E 's#/$##')
OWNER=$(echo "$clean" | cut -d/ -f1)
REPO=$(echo "$clean" | cut -d/ -f2)

if [[ -z "$OWNER" || -z "$REPO" ]]; then
  echo "Error: no pude extraer owner/repo de '$GITHUB_URL'" >&2
  exit 2
fi

API_URL="https://api.github.com/repos/${OWNER}/${REPO}"

echo "Obteniendo branch por defecto para ${OWNER}/${REPO}..."
default_branch=$(curl -sSfL "$API_URL" 2>/dev/null | sed -n 's/.*"default_branch":[[:space:]]*"\([^"]*\)".*/\1/p' || true)
if [[ -z "$default_branch" ]]; then
  echo "No se pudo obtener default_branch desde la API; probando 'main' y 'master'..."
  for b in main master; do
    url_test="https://raw.githubusercontent.com/${OWNER}/${REPO}/${b}/README.md"
    if curl -sSfL --head "$url_test" >/dev/null 2>&1; then
      default_branch=$b
      break
    fi
  done
fi

if [[ -z "$default_branch" ]]; then
  echo "No se encontró una rama válida (intenté main/master)." >&2
  exit 3
fi

echo "Usando rama: $default_branch"

# Try to fetch README (several common variants)
readme_raw=""
for name in README.md README.MD README.markdown README.rst README.txt; do
  raw_url="https://raw.githubusercontent.com/${OWNER}/${REPO}/${default_branch}/${name}"
  if readme_raw=$(curl -sSfL "$raw_url" 2>/dev/null); then
    echo "Encontrado: $name"
    break
  fi
done

if [[ -z "$readme_raw" ]]; then
  echo "No se pudo descargar README desde la rama '$default_branch'." >&2
  exit 4
fi

# Extract title from first H1 or fallback to repo name
title=$(echo "$readme_raw" | sed -n 's/^# \+//p' | sed -n '1p' || true)
if [[ -z "$title" ]]; then
  title="$REPO"
fi

# Convert markdown to a short plain-text summary: first paragraph without code blocks
# Remove code fences and images, simplify links to text
plain=$(echo "$readme_raw" \
  | awk 'BEGIN{in_code=0} /^```/ {in_code=!in_code; next} !in_code {print}' \
  | sed -E 's/!\[[^\]]*\]\([^\)]*\)//g' \
  | sed -E 's/\[([^\]]+)\]\([^\)]*\)/\1/g' \
  | sed -E 's/[*_]{1,2}//g' )

# Extract first non-empty paragraph
summary=$(echo "$plain" | awk 'BEGIN{RS=""} {gsub(/\n/," "); if(length($0)>20){print; exit}}')

# Truncate to ~300 chars for description
summary=$(echo "$summary" | sed -E 's/^[[:space:]]+|[[:space:]]+$//g' | cut -c1-300)

# Build slug from title
slug=$(echo "$title" | iconv -f utf8 -t ascii//TRANSLIT 2>/dev/null || echo "$title" )
slug=$(echo "$slug" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g' | sed -E 's/^-|-$//g')
if [[ -z "$slug" ]]; then
  slug="${OWNER}-${REPO}"
fi

out_dir="_projects"
mkdir -p "$out_dir"
out_file="$out_dir/${slug}.md"

if [[ -f "$out_file" ]]; then
  echo "Aviso: $out_file ya existe. Usando sufijo para no sobrescribir." >&2
  out_file="$out_dir/${slug}-$(date +%s).md"
fi

cat > "$out_file" <<EOF
---
layout: project
title: "${title}"
author: ""
repo: "${GITHUB_URL}"
type: ""
tech: ""
description: "${summary}"
permalink: "/projects/${slug}/"
---

<!-- Resumen generado automáticamente desde ${GITHUB_URL} -->

${summary}

> Fuente: ${GITHUB_URL}

EOF

echo "Proyecto creado: $out_file"
echo "Título: $title"
echo "Permalink: /projects/${slug}/"

exit 0
