from dotenv import load_dotenv
from openai import OpenAI
from src.prompts import PATIENT_SYSTEM_PROMPT

load_dotenv()

client = OpenAI()
conversation_history = []


def reset_conversation():
    conversation_history.clear()


def get_patient_response(agent_text: str) -> str:
    conversation_history.append({"role": "user", "content": agent_text})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": PATIENT_SYSTEM_PROMPT},
                *conversation_history,
            ],
            temperature=0.6,
        )

        patient_reply = response.choices[0].message.content

        if not patient_reply:
            patient_reply = "I'm sorry, could you repeat that?"

        patient_reply = patient_reply.strip()

    except Exception as e:
        print(f"OpenAI Error: {e}")
        patient_reply = "I'm sorry, could you repeat that?"

    conversation_history.append({"role": "assistant", "content": patient_reply})

    # Keep only the most recent conversation turns to limit token usage.
    if len(conversation_history) > 30:
        conversation_history[:] = conversation_history[-30:]

    print(f"Agent: {agent_text}")
    print(f"Patient: {patient_reply}")

    return patient_reply