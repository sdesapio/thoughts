#!/usr/bin/env python3
"""Copy the root SKILL.md and LICENSE into the Claude plugin folder."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parent.parent
COPIES = {"SKILL.md": "plugin/skills/thoughts/SKILL.md", "LICENSE": "plugin/LICENSE"}


def main():
    for source, destination in COPIES.items():
        target = ROOT / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / source, target)
        print(f"{source} -> {destination}")


if __name__ == "__main__":
    main()
