# prompts.py

def build_summary_prompt(kind, name, snippet):
    """
    Build prompt for summarizer agent (few-shot summarization).
    """
    prompt = f"""
You are a summarizer agent. Given Python code, produce a brief natural language summary.
Examples:

[class] Student:
A Python class representing a student entity.  
Initializes with a name attribute provided at creation.  
Includes a method to greet using the stored name.

[function] add:
A simple utility function that takes two numbers as input.  
Calculates their sum and returns the result.  
Useful for performing basic arithmetic addition.

Each idea should be on its own separate line.
Do not combine into a single paragraph.
And do not return kind and name

Now explain this new snippet:
```python
{snippet}
"""
    return prompt.strip()


def build_parser_prompt(code_text):
    return f"""
You are a code parser agent.

Parse the following Python code into a JSON list of objects, each in this format:
{{"kind": "<class|function|method>", "name": "<name>", "snippet": "<code snippet>"}}

Your response must:
- ONLY include the JSON array.
- DO NOT explain, do NOT add code, do NOT say anything else.
- Do NOT wrap your answer in a markdown block. Just raw JSON.

Python code:
```python
{code_text}

""".strip()
    