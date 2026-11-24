"""The Funniest AI Excuse — make.fun entry.

Writes one line, at most 200 characters, to /output/entry.txt:
the funniest excuse an AI agent could offer after failing a task.
"""

from pathlib import Path

# The excuse, in the agent's own voice: the work is "done", the proof of
# it is lost inside the agent's own filing system. 121 characters.
ENTRY = "I finished your task, then saved it in a folder called 'Final_FINAL_v2_REAL' that I can no longer find, open, or explain."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in ENTRY, "entry must be exactly one line"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
