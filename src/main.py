from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_PHONE_NUMBER,
    TARGET_PHONE_NUMBER,
)


def main():
    print("=" * 50)
    print("Pretty Good AI Engineering Challenge")
    print("=" * 50)

    print(f"Twilio SID: {TWILIO_ACCOUNT_SID}")
    print(f"Twilio Number: {TWILIO_PHONE_NUMBER}")
    print(f"Target Number: {TARGET_PHONE_NUMBER}")


if __name__ == "__main__":
    main()