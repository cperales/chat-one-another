import json
import requests
import re

OLLAMA_HOST = "http://localhost:11434"

# Load configuration for models and prompts
CONFIG_PATH = "config.json"
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    _cfg = json.load(f)

MODEL_A = _cfg.get("model_a", "qwen3:latest")
MODEL_B = _cfg.get("model_b", "qwen3:latest")
INITIAL_PROMPT = _cfg.get("initial_prompt", "Hi! How are you?")
ITERATIONS = int(_cfg.get("iterations", 100))
CHAT_HISTORY_FILE = _cfg.get("chat_history", "chat_history.md")


def remove_think_tags(text):
    # Remove <think>...</think> blocks
    cleaned = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    # Optional: clean up extra whitespace
    cleaned = re.sub(r'\n\s*\n', '\n\n', cleaned)  # Replace multiple newlines
    return cleaned.strip()


def query_ollama(model, prompt, history):
    url = f"{OLLAMA_HOST}/v1/chat/completions"
    payload = {
        "model": model,
        "messages": history + [{"role": "user", "content": prompt}],
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    content = data['choices'][0]['message']['content']
    content = remove_think_tags(content)
    return content, history


def main(initial_prompt=INITIAL_PROMPT):
    print(f"Initial prompt: {initial_prompt}")
    with open(CHAT_HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(f"### Loop 0\n")
            f.write(f"**Initial prompot**:\n{initial_prompt}\n\n")
    history_a = list()
    history_b = list()
    response_b = initial_prompt

    for i in range(1, ITERATIONS + 1):
        print(f"\n=== Loop {i} ===")
        # Send model B's response to model A
        response_a, history_a = query_ollama(MODEL_A, response_b, history=history_a)
        print(f"Response from A ({MODEL_A}):\n{response_a}\n")

        print("-" * 20)
        # Send model A's response to model B
        response_b, history_b = query_ollama(MODEL_B, response_a, history=history_b)
        print(f"Response from B ({MODEL_B}):\n{response_b}\n")

        with open(CHAT_HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(f"### Loop {i}\n")
            f.write(f"**A ({MODEL_A})**:\n{response_a}\n\n")
            f.write(f"**B ({MODEL_B})**:\n{response_b}\n\n")

if __name__ == "__main__":
    main()
