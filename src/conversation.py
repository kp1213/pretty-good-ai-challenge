from dotenv import load_dotenv
from openai import OpenAI
from src.prompts import PATIENT_SYSTEM_PROMPT

load_dotenv()

client = OpenAI()

def get_patient_response(agent_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": PATIENT_SYSTEM_PROMPT},
            {"role": "user", "content": agent_text},
        ],
    )

    return response.choices[0].message.content