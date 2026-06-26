from src.caller import place_call


def main():
    print("=" * 50)
    print("Pretty Good AI Engineering Challenge")
    print("=" * 50)

    call_sid = place_call()
    print(f"Call SID: {call_sid}")


if __name__ == "__main__":
    main()