from datetime import datetime
from pathlib import Path

REPORTS_DIR = Path("reports")


def generate_bug_report(transcript_path: Path) -> Path:
    REPORTS_DIR.mkdir(exist_ok=True)

    transcript_text = transcript_path.read_text(encoding="utf-8")
    report_name = transcript_path.stem.replace("call_", "bug_report_") + ".md"
    report_path = REPORTS_DIR / report_name

    agent_turns = transcript_text.count("Agent:")
    patient_turns = transcript_text.count("Patient:")

    report = f"""# Bug Report

## Metadata

- Generated at: {datetime.now().isoformat()}
- Transcript: `{transcript_path}`
- Agent turns: {agent_turns}
- Patient turns: {patient_turns}

## Conversation Summary

Patient bot attempted to complete a healthcare phone interaction using the saved transcript.

## Potential Issues Observed

- [ ] Agent misunderstood patient information
- [ ] Agent repeated a question unnecessarily
- [ ] Agent failed to complete the requested task
- [ ] Agent transferred or ended the call unexpectedly
- [ ] Patient response sounded unnatural
- [ ] Speech recognition issue occurred

## Notes

Review the transcript and fill in the specific bugs found during the call.

## Transcript Reference

```text
{transcript_text}
```
"""

    report_path.write_text(report, encoding="utf-8")
    return report_path
