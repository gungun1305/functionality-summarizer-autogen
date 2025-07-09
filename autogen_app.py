# autogen_app.py
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from autogen import AssistantAgent
from parser import parse_code
from prompts import build_summary_prompt

config_list = [
    {"model": "gpt-4o-mini", "api_key": OPENAI_API_KEY}
]

summarizer_agent = AssistantAgent(
    name="summarizer",
    llm_config={"config_list": config_list}
)

def main():
    # Read code to analyze
    with open("code_samples/example.py", "r", encoding="utf-8") as f:
        code_text = f.read()

    parts = parse_code(code_text)

    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write("Functionality Summarizer\n\n")

        for kind, name, snippet in parts:
            prompt = build_summary_prompt(kind, name, snippet)

            summary = summarizer_agent.generate_reply(
                messages=[{"role": "user", "content": prompt}]
            )
            summary = str(summary).strip()

            line = f"[{kind}] {name}:\n{summary}\n\n"
            print(line.strip())
            f.write(line)

    print("\n All summaries saved to summary.txt")

if __name__ == "__main__":
    main()
