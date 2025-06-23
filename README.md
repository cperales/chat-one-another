# Chat One Another

This repository contains a simple Python script that lets two local language models talk to each other using [Ollama](https://ollama.com/).

## Requirements

- Python 3
- The `requests` package (install via `pip install -r requirements.txt`)
- An Ollama server running at `http://localhost:11434`

## Usage

1. Install the required Python package:
   ```bash
   pip install -r requirements.txt
   ```
2. Optionally edit `script.py` to adjust the models (`MODEL_A` and `MODEL_B`) or the starting prompt.
3. Run the script:
   ```bash
   python script.py
   ```
4. Conversation turns are logged to `chat_history.md` in Markdown format.

## Project Files

- `script.py` – orchestrates the conversation between the two models.
- `requirements.txt` – lists the Python dependency.
- `chat_history.md` – created when the script runs and stores the dialogue.

