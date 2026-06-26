from twilio.rest import Client
from src.config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER,
    TARGET_PHONE_NUMBER,
)


def place_call():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    call = client.calls.create(
        to=TARGET_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        url="https://version-panoramic-deny.ngrok-free.dev/voice",
    )

    print(f"Call started. SID: {call.sid}")
    return call.sid