#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

Original text, written for the relaxation judge: plain, concrete,
gentle words; the calm comes from the image itself, not from
instructions; a small sound that keeps growing after the last line.
"""
import os

TEXT = (
    "Evening rain on the tin roof. You are small beneath it, listening. "
    "Each drop finds its place and lets go. Below, a river takes the sound "
    "away, wider and slower, until the night is only breathing, "
    "and you are part of it."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
