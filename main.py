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


def main():
    out_dir = output_directory()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in text, "entry must be one line"
    assert text.endswith("."), "entry must end as one sentence"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    verify(path, text)


def verify(path, expected):
    """Read the file back and confirm it holds exactly the entry line."""
    with open(path, encoding="utf-8", newline="\n") as f:
        written = f.read()
    assert written == expected + "\n", "entry.txt does not match the line"
    print(path)
    print(expected)


if __name__ == "__main__":
    os.umask(0o022)
    main()
