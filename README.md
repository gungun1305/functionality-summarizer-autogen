# 🧐 Functionality Summarizer (AutoGen + OpenAI)

This project parses Python code into parts (classes, functions) and then generates clear, multiline summaries for each part — using the [AutoGen](https://github.com/microsoft/autogen) framework and OpenAI GPT-4o-mini.

It was built as a learning project to explore: ✅ code parsing,\
✅ few-shot prompting,\
✅ and summarization using LLMs.

---

## 📦 Project structure

```
functionality-summarizer-openai/
├── autogen_app.py        # Main script: parses code & creates summaries
├── parser.py             # Parser agent: finds classes/functions in code
├── prompts.py            # Prompt templates for parser & summarizer
├── code_samples/
│   └── example.py        # Sample Python code to test
├── summary.txt           # Output: generated summaries
└── README.md
```

---

## ⚙ Setup

1. **Clone / download** this repository.

2. Install dependencies:

   ```bash
   pip install ag2
   ```

   *(You may also need **`openai`** if not included: **`pip install openai`**)*

3. Replace the placeholder:

   ```python
   OPENAI_API_KEY = "sk-..."
   ```

   with your actual OpenAI API key (from your OpenAI dashboard).

---

## 🚀 How to run

From the project folder:

```bash
python autogen_app.py
```

✅ The script will:

- Read the Python file in `code_samples/example.py`
- Parse it into parts
- Generate multiline summaries
- Save everything to `summary.txt`

---

## ✏ How it works

- **parser\_agent** (in `parser.py`):\
  Uses AutoGen's `AssistantAgent` to parse the raw code into JSON objects.
- **summarizer\_agent** (in `autogen_app.py`):\
  Uses another `AssistantAgent` to create detailed, multiline summaries.
- **prompts.py**:\
  Stores prompt templates with few-shot examples.

---

## 📜 Example output

```
=== Functionality Summarizer (AutoGen, few-shot) ===

[class] Student:
A Python class representing a student entity.
Initializes with a name attribute provided during creation.
Includes a greet method to print a personalized greeting.

[function] add:
A utility function that takes two numbers.
Calculates and returns their sum.
Useful for basic arithmetic.
```

---

## 🧹 Credits & tools

- [AutoGen (Microsoft)](https://github.com/microsoft/autogen)
- [OpenAI GPT-4o-mini](https://platform.openai.com)
- Python 3.8+

---

## ✅ Notes

- This project was built as a demo / academic project.
- Remember: using someone else’s API key still consumes tokens and may cost money.

---

Feel free to fork, improve, or adapt!


