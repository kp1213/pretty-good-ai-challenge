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

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": PATIENT_SYSTEM_PROMPT},
            *conversation_history,
        ],
    )

    patient_reply = response.choices[0].message.content or ""
    patient_reply = patient_reply.strip()

    conversation_history.append({"role": "assistant", "content": patient_reply})

    if len(conversation_history) > 20:
        conversation_history[:] = conversation_history[-20:]

    return patient_reply