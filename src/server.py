from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
from src.conversation import get_patient_response, reset_conversation
from src.transcript_logger import start_transcript, log_turn, get_current_transcript_path
from src.bug_report import generate_bug_report

app = Flask(__name__)


@app.route("/voice", methods=["POST"])
def voice():
    reset_conversation()
    transcript_path = start_transcript()
    print(f"Transcript started: {transcript_path}")
    response = VoiceResponse()

    gather = Gather(
        input="speech",
        action="/respond",
        method="POST",
        timeout=8,
        speech_timeout="auto",
    )

    gather.say(
        "Hello. This is the patient bot. I am ready to begin the call.",
        voice="alice",
    )

    response.append(gather)

    response.say("I did not hear anything. Goodbye.", voice="alice")
    return str(response)


@app.route("/respond", methods=["POST"])
def respond():
    agent_text = request.form.get("SpeechResult", "")
    print(f"Agent said: {agent_text}")
    log_turn("Agent", agent_text)

    patient_reply = get_patient_response(agent_text)
    print(f"Patient replied: {patient_reply}")
    log_turn("Patient", patient_reply)

    response = VoiceResponse()

    gather = Gather(
        input="speech",
        action="/respond",
        method="POST",
        timeout=8,
        speech_timeout="auto",
    )

    gather.say(patient_reply, voice="alice")
    response.append(gather)

    response.say("Goodbye.", voice="alice")

    transcript_path = get_current_transcript_path()

    if transcript_path is not None:
        report_path = generate_bug_report(transcript_path)
        print(f"Bug report generated: {report_path}")

    return str(response)

if __name__ == "__main__":
    app.run(port=5050, debug=True)