#!/usr/bin/env python3
"""Block PRs where users edit projects they do not own.

Ownership is defined by one of these fields in front matter (TOML):
- owner_github (recommended)
- params.author.github_username
- params.author.github_url (username inferred from URL)
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tomllib
from typing import Any


def run_cmd(args: list[str]) -> str:
    return subprocess.check_output(args, text=True).strip()


def changed_project_files(base_sha: str, head_sha: str) -> list[tuple[str, str]]:
    out = run_cmd(["git", "diff", "--name-status", base_sha, head_sha, "--", "content/proyectos/**/*.md"])
    rows: list[tuple[str, str]] = []
    if not out:
        return rows
    for line in out.splitlines():
        parts = line.split("\t")
        status = parts[0]
        path = parts[-1]
        rows.append((status, path))
    return rows


def read_file_from_ref(git_ref: str, path: str) -> str | None:
    try:
        return run_cmd(["git", "show", f"{git_ref}:{path}"])
    except subprocess.CalledProcessError:
        return None


def read_file_from_head(path: str) -> str | None:
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_toml_front_matter(markdown: str) -> dict[str, Any]:
    # Hugo TOML front matter is delimited by +++
    match = re.match(r"\A\+\+\+\s*\n(.*?)\n\+\+\+", markdown, re.DOTALL)
    if not match:
        return {}
    try:
        return tomllib.loads(match.group(1))
    except tomllib.TOMLDecodeError:
        return {}


def normalize_username(raw: str | None) -> str:
    if not raw:
        return ""
    value = raw.strip().lower().lstrip("@")
    if value.startswith("https://github.com/"):
        value = value[len("https://github.com/") :]
    if value.startswith("http://github.com/"):
        value = value[len("http://github.com/") :]
    value = value.strip("/")
    # Remove URL path suffix if present, keeping username only.
    if "/" in value:
        value = value.split("/", 1)[0]
    return value


def get_owner_username(front_matter: dict[str, Any]) -> str:
    owner = normalize_username(front_matter.get("owner_github"))
    if owner:
        return owner

    params = front_matter.get("params") or {}
    author = params.get("author") if isinstance(params, dict) else {}
    if not isinstance(author, dict):
        return ""

    owner = normalize_username(author.get("github_username"))
    if owner:
        return owner

    owner = normalize_username(author.get("github_url"))
    return owner


def fail(message: str) -> None:
    print(f"::error::{message}")
    sys.exit(1)


def main() -> None:
    base_sha = os.environ.get("BASE_SHA", "")
    head_sha = os.environ.get("HEAD_SHA", "")
    actor = normalize_username(os.environ.get("GITHUB_ACTOR", ""))

    if not base_sha or not head_sha or not actor:
        fail("Missing BASE_SHA, HEAD_SHA or GITHUB_ACTOR in environment.")

    files = changed_project_files(base_sha, head_sha)
    if not files:
        print("No project files changed.")
        return

    for status, path in files:
        if status.startswith("A"):
            head_content = read_file_from_head(path)
            if not head_content:
                fail(f"Could not read new file content for validation: {path}")

            head_fm = extract_toml_front_matter(head_content)
            head_owner = get_owner_username(head_fm)
            if not head_owner:
                fail(
                    f"{path} is missing owner info. Add owner_github = '{actor}' in front matter."
                )
            if head_owner != actor:
                fail(
                    f"Ownership validation failed for new file {path}. "
                    f"GitHub actor '{actor}' must match owner '{head_owner}'."
                )
            continue

        if status.startswith("D"):
            base_content = read_file_from_ref(base_sha, path)
            if not base_content:
                fail(f"Could not read deleted file from base for validation: {path}")

            base_fm = extract_toml_front_matter(base_content)
            base_owner = get_owner_username(base_fm)
            if not base_owner:
                fail(f"Deleted file {path} has no owner metadata in base branch.")
            if base_owner != actor:
                fail(
                    f"Ownership validation failed for delete {path}. "
                    f"GitHub actor '{actor}' cannot delete file owned by '{base_owner}'."
                )
            continue

        base_content = read_file_from_ref(base_sha, path)
        head_content = read_file_from_head(path)
        if not base_content or not head_content:
            fail(f"Could not read both base and head versions for validation: {path}")

        base_fm = extract_toml_front_matter(base_content)
        head_fm = extract_toml_front_matter(head_content)
        base_owner = get_owner_username(base_fm)
        head_owner = get_owner_username(head_fm)

        if not base_owner:
            fail(f"{path} has no owner metadata in base branch.")
        if not head_owner:
            fail(f"{path} is missing owner metadata in PR changes.")

        if base_owner != head_owner:
            fail(
                f"Ownership field change is not allowed in {path}. "
                f"Base owner is '{base_owner}' and PR owner is '{head_owner}'."
            )

        if base_owner != actor:
            fail(
                f"Ownership validation failed for {path}. "
                f"GitHub actor '{actor}' can only edit files owned by '{actor}', but file owner is '{base_owner}'."
            )

    print("Ownership validation passed.")


if __name__ == "__main__":
    main()
