from datetime import datetime
from pathlib import Path

TRANSCRIPTS_DIR = Path("transcripts")

current_transcript_path = None


def start_transcript() -> Path:
    global current_transcript_path

    TRANSCRIPTS_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    current_transcript_path = TRANSCRIPTS_DIR / f"call_{timestamp}.txt"

    with open(current_transcript_path, "w", encoding="utf-8") as file:
        file.write("Pretty Good AI Challenge Call Transcript\n")
        file.write(f"Started at: {datetime.now().isoformat()}\n")
        file.write("=" * 50 + "\n\n")

    return current_transcript_path


def log_turn(speaker: str, text: str) -> None:
    if not text:
        return

    if current_transcript_path is None:
        start_transcript()

    with open(current_transcript_path, "a", encoding="utf-8") as file:
        file.write(f"{speaker}:\n{text}\n\n")


def get_current_transcript_path():
    return current_transcript_path