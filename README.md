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
2. Add a `config.json` to adjust the models (`model_a` and `model_b`), the starting prompt, the number of conversation turns, or the output file name. You can copy the `config.json.example`.
   ```bash
   cp config.json.example config.json
   ```

3. Run the script:
   ```bash
   python script.py
   ```
   The assistant responses will stream to the console as they are generated.
4. Conversation turns are logged to the file specified by `chat_history` in `config.json`.

## Project Files

- `config.json` – stores model names, the initial prompt, iteration count, and output file location.
- `script.py` – orchestrates the conversation between the two models.
- `requirements.txt` – lists the Python dependency.
- history file (default `chat_history.md`) – created when the script runs and stores the dialogue.

