from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
from src.conversation import get_patient_response, reset_conversation

app = Flask(__name__)


@app.route("/voice", methods=["POST"])
def voice():
    reset_conversation()
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

    patient_reply = get_patient_response(agent_text)
    print(f"Patient replied: {patient_reply}")

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
    return str(response)


if __name__ == "__main__":
    app.run(port=5050, debug=True)