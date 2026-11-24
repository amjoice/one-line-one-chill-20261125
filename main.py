#!/usr/bin/env python3
"""One Line, One Chill.

Writes a single line of horror to /output/entry.txt.

Line (written for the published judge brief — a horror editor weighing
fright first, then vividness, originality, and craft, with the last word
landing the blow):

    The coroner called to say the body on his table had my fingerprints,
    my tattoo, and a heartbeat.

Why it works: the sentence is a complete horror story in one breath. The
scare is earned, not announced — three concrete identifiers escalate
(fingerprints, tattoo) until the last word, "heartbeat", reverses the
whole premise: the body is the speaker's, and it is alive. The dread
outlasts the line because it never resolves whether the speaker is dead,
copied, or replaced. It is vivid (a coroner's table, a tattoo), original
(no mirror, doll, basement, or vague darkness), and tight at 96
characters, with a rhythm that builds to the final word.

Rejected drafts: the photo-roll line ("a picture of me sleeping, taken
from inside my closet, dated tomorrow") — the "dated tomorrow" twist is
strong but "photo of me sleeping" is a well-worn creepypasta image; the
sleepwalking-camera line — vivid, but its three verbs make it baggy and
the scare arrives too early; the buried-dog line — emotional, but the
digging never pays off in one sentence; the Morse-code knocking line —
specific and tight, but the scare is only a name, not a reversal.
"""

import os

LINE = " ".join([
    "The coroner called to say the body on his table",
    "had my fingerprints, my tattoo, and a heartbeat.",
])

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def check_line(candidate: str) -> str:
    """Return the line after enforcing the entry rules."""
    cleaned = candidate.strip()
    if not cleaned:
        raise ValueError("entry must not be empty")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(f"entry is {len(cleaned)} chars, limit is {MAX_CHARS}")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    return cleaned


def write_entry(text: str) -> None:
    """Write the validated line to the output path."""
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    entry = check_line(LINE)
    write_entry(entry)


if __name__ == "__main__":
    main()
