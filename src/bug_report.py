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

    total_turns = agent_turns + patient_turns

    report = f"""# Bug Report

## Metadata

- Generated at: {datetime.now().isoformat(timespec="seconds")}
- Transcript file: `{transcript_path}`
- Agent turns: {agent_turns}
- Patient turns: {patient_turns}
- Total conversation turns: {total_turns}

## Conversation Summary

The patient bot attempted to complete a healthcare phone interaction as Alex Johnson, a patient seeking an acute visit for a cough and sore throat.

## Test Objective

Evaluate whether the healthcare phone agent can:
- Understand the patient's request
- Collect required patient information
- Handle appointment scheduling
- Avoid unnecessary repetition
- Respond appropriately to clarification requests
- Complete the call without confusion or premature termination

## Outcome

- [ ] Successful appointment scheduled
- [ ] Partial completion
- [ ] Failed to complete task
- [ ] Call ended unexpectedly
- [ ] Needs manual review

## Potential Issues Observed

- [ ] Agent misunderstood patient information
- [ ] Agent repeated a question unnecessarily
- [ ] Agent failed to complete the requested task
- [ ] Agent ignored or mishandled clarification
- [ ] Agent provided unclear instructions
- [ ] Agent transferred or ended the call unexpectedly
- [ ] Patient response sounded unnatural
- [ ] Speech recognition issue occurred
- [ ] Long silence or awkward delay occurred
- [ ] Other issue

## Bug Details

### Bug 1

- **Title:** 
- **Severity:** Low / Medium / High
- **What happened:** 
- **Expected behavior:** 
- **Actual behavior:** 
- **Evidence from transcript:** 
- **Possible cause:** 
- **Suggested improvement:** 

### Bug 2

- **Title:** 
- **Severity:** Low / Medium / High
- **What happened:** 
- **Expected behavior:** 
- **Actual behavior:** 
- **Evidence from transcript:** 
- **Possible cause:** 
- **Suggested improvement:** 

## Reviewer Notes

Add any additional observations about call quality, realism, transcription accuracy, or agent behavior.

## Transcript Reference

```text
{transcript_text}
```
"""

    report_path.write_text(report, encoding="utf-8")
    return report_path