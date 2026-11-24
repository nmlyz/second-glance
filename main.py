#!/usr/bin/env python3
"""Write one sentence pitching a bizarre startup idea to /output/entry.txt.

The line is a single sentence of at most 200 characters: a startup idea
that sounds absurd at first glance, until the business behind it lands.
It names the odd thing being sold, who pays for it, and why it holds
together: empty church pews, rented by the day as silent desks for
remote workers, with the only networking event on Sunday.
"""

import os

LINE = (
    "We rent out empty church pews as silent co-working desks \u2014 "
    "$12 a day, Wi-Fi included, and the only networking event is Sunday."
)


def output_directory():
    """The directory the entry is written to, /output unless overridden."""
    return os.environ.get("OUTPUT_DIR", "/output")


def build_entry():
    """Assemble the entry line from its parts and return it stripped."""
    return LINE.strip()


def validate_entry(text):
    """Check the entry line against every rule of the brief."""
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in text, "entry must be one line"
    assert text.endswith("."), "entry must end as one sentence"
    return text


def write_entry(path, text):
    """Write the entry line plus a trailing newline, fixed permissions."""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    return path


def main():
    out_dir = output_directory()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = validate_entry(build_entry())
    write_entry(path, text)
    verify_entry(path, text)


def verify_entry(path, expected):
    """Read the file back and confirm it holds exactly the entry line.

    The written bytes are re-validated against the same rules as the
    in-memory line, so a truncated or altered write cannot slip through.
    """
    with open(path, encoding="utf-8", newline="\n") as f:
        written = f.read()
    assert written == expected + "\n", "entry.txt does not match the line"
    validate_entry(written.rstrip("\n"))
    print(path)
    print(expected)
    print(f"chars: {len(expected)}")


if __name__ == "__main__":
    os.umask(0o022)
    main()
