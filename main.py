"""Entry program for the 21 November 2026 world-news image.

Reads the news image bundled in this repository and writes it,
byte for byte, to /output/entry.png. No network access, no
randomness: running it twice produces identical output.
"""

import hashlib
import shutil
from pathlib import Path

IMAGE = Path(__file__).parent / "news.png"
TARGET = Path("/output/entry.png")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(IMAGE, TARGET)
    if digest(IMAGE) != digest(TARGET):
        raise SystemExit("entry.png does not match news.png")
    print("entry written:", TARGET, f"({TARGET.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
