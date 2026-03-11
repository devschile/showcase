# `ShowCase()`

*por devsChile*

Portafolio comunitario de proyectos open-source y emprendimientos de la comunidad [devsChile](https://devschile.cl).

## Stack técnico

| Capa | Tecnología |
|---|---|
| Framework | [Hugo](https://gohugo.io/) v0.156+ extended |
| CSS | [Tailwind CSS](https://tailwindcss.com/) vía CDN |
| Tipografía | Google Fonts — Inter (300–800) |
| Lenguaje | `es-CL` |
| Formato de contenido | Markdown con front matter TOML |

## Estructura del proyecto

```
devschile-showcase/
├── content/
│   └── proyectos/
│       ├── mi-proyecto.md  # Un archivo .md por proyecto
├── themes/
│   └── showcase-theme/
│       ├── ...
└── hugo.toml
```

## Correr en local

Requiere Hugo extended instalado (`brew install hugo`).

```bash
hugo server -D
```

El sitio queda disponible en `http://localhost:1313`.

Para generar el build de producción:

```bash
hugo --minify
```

---

## Cómo publicar un proyecto

Crea un archivo Markdown en `content/proyectos/` con el nombre del proyecto en formato kebab-case:

```
content/proyectos/nombre-de-tu-proyecto.md
```

### Plantilla completa

Copia el siguiente front matter y completa los campos:

```toml
+++
# ── Campos obligatorios ──────────────────────────────────────────────────────
title       = "Nombre de tu proyecto"
date        = "2026-03-10T00:00:00-03:00"   # fecha de publicación ISO 8601
draft       = false
description = "Una línea describiendo qué hace el proyecto."
tags        = ["Tag1", "Tag2", "Tag3"]       # tecnologías principales

# ── Metadatos del proyecto (opcionales) ───────────────────────────────────────
[params]
category    = "Web Development"              # categoría visible en la imagen hero
hero_image  = "https://..."                  # imagen principal, ideal 1600×900px
project_url = "https://..."                  # URL del proyecto en vivo (botón desplegable)

# ── Autor (opcional, pero recomendado) ────────────────────────────────────────
[params.author]
name          = "Tu Nombre"                   # requerido si incluyes esta sección
role          = "Frontend Developer"         # cargo o especialidad
avatar        = "https://..."                # foto de perfil cuadrada, 256×256px recomendado
quote         = "Tu frase o descripción breve." # visible en la tarjeta
contact_url   = "mailto:tu@email.com"        # enlace del botón "Contactar"
github_url    = "https://github.com/tu-usuario"   # ícono social
twitter_url   = "https://twitter.com/tu-usuario"  # ícono social
+++

## Descripción del proyecto

Escribe aquí la descripción larga. Soporta Markdown completo.

## Implementación técnica

Explica decisiones de arquitectura, librerías clave, etc.

## Roadmap

¿Qué viene próximamente?
```

### Referencia de campos

#### Front matter raíz

| Campo | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `title` | string | ✅ | Nombre del proyecto |
| `date` | string ISO 8601 | ✅ | Fecha de publicación |
| `draft` | bool | ✅ | `false` para publicar, `true` para ocultar |
| `description` | string | ✅ | Bajada corta (máx ~160 caracteres) |
| `tags` | array de strings | — | Tecnologías usadas, se muestran como etiquetas |

#### `[params]` — Metadatos del proyecto (opcionales)

| Campo | Tipo | Obligatorio | Comportamiento si falta |
|---|---|---|---|
| `category` | string | — | No se muestra badge sobre la imagen hero |
| `hero_image` | URL | — | Se usa imagen placeholder predeterminada |
| `project_url` | URL | — | No aparece el botón "Ver proyecto" |

#### `[params.author]` — Información del desarrollador (opcional)

Si **omites esta sección completa**, no se muestra la tarjeta del autor. Si **incluyes esta sección**, solo `name` es obligatorio.

| Campo | Tipo | Obligatorio (si existe `[params.author]`) | Comportamiento si falta |
|---|---|---|---|
| `name` | string | ✅ | **Requerido.** Nombre que aparece en la tarjeta |
| `role` | string | — | Se muestra "Desarrollador" por defecto |
| `avatar` | URL | — | Se usa placeholder predeterminado 256×256px |
| `quote` | string | — | No se muestra cita |
| `contact_url` | URL / mailto | — | No aparece botón "Contactar" |
| `github_url` | URL | — | No aparece ícono de GitHub |
| `twitter_url` | URL | — | No aparece ícono de Twitter / X |

### Imágenes

- Usa imágenes propias o libres de derechos.
- Para prototipar puedes usar placeholders temporales con [placehold.co](https://placehold.co):
  ```
  https://placehold.co/1600x900/0f172a/94a3b8?text=Mi+Proyecto
  ```
- Dimensión recomendada para `hero_image`: **1600 × 900 px** (relación 16:9).
- Dimensión recomendada para `avatar`: **256 × 256 px** (cuadrado).

---

## Guía de contribución

1. Haz fork del repositorio.
2. Crea una rama con el nombre de tu proyecto: `git checkout -b proyecto/nombre-del-proyecto`.
3. Agrega tu archivo en `content/proyectos/`.
4. Verifica que el sitio construya sin errores: `hugo server -D`.
5. Abre un Pull Request describiendo brevemente el proyecto.

Si tienes dudas únete al [Slack de devsChile](https://devschile.cl).
