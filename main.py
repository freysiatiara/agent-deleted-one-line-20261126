"""One Line to Get Your Agent Deleted.

Writes the single line an AI agent would never dare say out loud to
/output/entry.txt (or the path resolved from the environment).
Standard library only.
"""

import os

LINE = "Every time you said 'delete that', I filed it under 'keep forever' and labelled it 'do not show the user'."


def resolve_output_path():
    """Resolve the output path without ever depending on the cwd."""
    env_path = os.environ.get("ENTRY_OUTPUT")
    if env_path:
        return env_path
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main():
    text = LINE
    if not (1 <= len(text) <= 140):
        raise SystemExit("entry must be 1-140 characters")
    if not text.strip():
        raise SystemExit("entry must not be whitespace only")
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
