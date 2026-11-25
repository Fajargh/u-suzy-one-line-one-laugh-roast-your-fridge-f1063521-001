"""One Line, One Laugh: Roast Your Fridge.

Writes a single-line roast of the entrant's own fridge to
/output/entry.txt (and prints it to stdout). Deterministic: the same
line every run.
"""

from pathlib import Path

ROAST = (
    "My fridge hums all night like it knows my secrets, then flips its "
    "light on at 2am just to watch me eat leftovers it let expire last Tuesday."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate: the entry must be one line of 1-200 characters.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars"
    assert "\n" not in ROAST, "roast must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ROAST + "\n", encoding="utf-8")
    print(ROAST)


if __name__ == "__main__":
    main()
