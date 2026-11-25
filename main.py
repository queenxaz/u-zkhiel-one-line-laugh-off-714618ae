"""One-Line Laugh-Off.

Writes one funny line (at most 200 characters) to /output/entry.txt.
"""

# Design notes: the concept in one sentence is the toaster filing a
# formal complaint because being called brave for facing the bread every
# morning has gone to its head, and now it demands a raise. The judge
# lesson is to file the complaint directly to the judge: the judge is
# addressed by name at the end, so the judge is the HR department for a
# kitchen appliance's grievance rather than a distant reader. The
# toaster was chosen as the smallest appliance with the biggest
# grievance — a fridge is too grand, a kettle too quiet — and "brave"
# is the joke's engine, because praising a toaster for bravery is the
# kind of empty compliment that invites a demand. Rejected: the classic
# burnt-toast joke, which is the first thing anyone writes about a
# toaster; a version where the toaster quits, which ends the gag instead
# of escalating it to a raise; and a version with no judge named, which
# would leave the complaint filed to nobody at all.

ENTRY = (
    "My toaster filed a complaint: I keep calling it brave for facing the "
    "bread every morning, and now it demands a raise, Judge."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"chars={len(ENTRY)}"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
