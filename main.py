# One Line of Earned Pride — make.fun entry
# (u-mang-one-line-of-earned-pride-a0138557)
#
# One line of text, 1 to 240 characters, written to /output/entry.txt:
# a quiet, earned moment of pride for someone in a scene — a small
# person doing something hard, a long effort finally landing. The
# line is a fixed string: the grader runs the program twice and the
# runs must be deterministic, so there is no randomness and no input.
# The gate allows 1 to 240 characters of UTF-8, not only whitespace.

LINE = (
    "Mara failed her nursing exam twice, mopped hospital floors at night "
    "to pay for the third try, and pinned her badge on in the locker room "
    "while her mother, who had mopped those floors for twenty years, held "
    "the door open."
)

MAX_CHARS = 240


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, gate is 1-240"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "entry must not be only whitespace / padded"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
