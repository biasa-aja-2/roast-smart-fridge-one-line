"""Roast the Smart Fridge: one line, best laugh wins.

Writes a single-line roast of the smart fridge to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Gate: UTF-8 text, 1-160 chars, not whitespace-only, one line.
Pure stdlib only.
"""
import os
import sys

# 156 chars (limit 160; 158 bytes, the em dash is 3 bytes). One sentence, one line, no trailing newline.
LINE = ("My smart fridge sent me a weekly health report, locked the ice "
        "dispenser, and still couldn't tell me where the leftovers went "
        "\u2014 it just watched me eat them.")


def main():
    if not (1 <= len(LINE) <= 160):
        print(f"gate fail: {len(LINE)} chars (need 1-160)", file=sys.stderr)
        return 1
    if LINE.strip() == "" or "\n" in LINE or "\r" in LINE:
        print("gate fail: not a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    out_path = out_dir if out_dir.endswith(".txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Byte-exact read-back verification.
    with open(out_path, encoding="utf-8") as f:
        got = f.read()
    assert got == LINE, "read-back mismatch"
    print(f"wrote {len(LINE)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
