import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

import json
from autogen import AssistantAgent
from prompts import build_parser_prompt

config_list = [
    {"model": "gpt-4o-mini", "api_key": OPENAI_API_KEY}
]

parser_agent = AssistantAgent(
    name="parser",
    llm_config={"config_list": config_list}
)

def parse_code(code_text):
    prompt = build_parser_prompt(code_text)
    
    response = parser_agent.generate_reply(
        messages=[{"role": "user", "content": prompt}]
    )
    text = str(response).strip()

    # Remove ```json ... ``` if present
    if text.startswith("```json"):
        text = text.removeprefix("```json").removesuffix("```").strip()

    try:
        parsed_list = json.loads(text)
        return [(item["kind"], item["name"], item["snippet"]) for item in parsed_list]
    except Exception:
        print("⚠️ Could not parse JSON. Raw output:")
        print(text)
        return []