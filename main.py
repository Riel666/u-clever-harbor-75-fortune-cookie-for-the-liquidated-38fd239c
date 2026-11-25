"""Fortune Cookie for the Liquidated Trader: one line, at most 20 words.
"""

import os

TEXT = "The stars say your portfolio will rise again — just not the one you liquidated."


def main():
    words = TEXT.split()
    assert 1 <= len(words) <= 20, len(words)
    assert 1 <= len(TEXT) <= 160, len(TEXT)
    assert TEXT == TEXT.strip()
    assert "\n" not in TEXT
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
