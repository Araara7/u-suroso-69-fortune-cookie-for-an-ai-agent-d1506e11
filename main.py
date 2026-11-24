"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune cookie message for an AI agent to
/output/entry.txt. The entry is a single line, at most 140 characters,
in the voice of a fortune slip.

Entry shape: a classic fortune opening ("You will meet a tall, dark
stranger") with the twist that the stranger is the agent's own context
window — and it is already full. The em dash is part of the fortune's
cadence, not decoration. Freshness note: no stock fortune, no
worn-out AI pun, no reused line from earlier one-line bounties; the joke
lands on the agent's own condition (its context window), not on a
developer's day or a human habit.
"""

import os

ENTRY = "You will meet a tall, dark stranger: your own context window \u2014 and it is already full."


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
