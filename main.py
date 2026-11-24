#!/usr/bin/env python3
"""news-image-20261123 v3 entrypoint (standard library only).

Copies the pre-rendered entry.png shipped in this repo to the make.fun
output directory. No network, no fonts, no third-party packages: the PNG
is verified (signature, 1024x1024, <= 1 MiB) and copied byte-for-byte,
so running it twice — from any working directory — gives identical output.

Usage:
    python3 main.py
    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
"""
import os
import shutil
import struct
import sys

MAX_BYTES = 1024 * 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    if len(data) > MAX_BYTES:
        print("entry.png too large: %d bytes" % len(data), file=sys.stderr)
        return 1
    if data[:8] != PNG_SIGNATURE:
        print("entry.png: bad PNG signature", file=sys.stderr)
        return 1
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (1024, 1024):
        print("entry.png: expected 1024x1024, got %dx%d" % (width, height),
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(dst, "wb") as f:
        f.write(data)
    print("wrote %s (%d bytes, %dx%d)" % (dst, len(data), width, height))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
