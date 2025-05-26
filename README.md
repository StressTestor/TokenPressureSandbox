
# Token Pressure Sandbox (CLI)

Analyze your prompts before you blow the context window.

## Features

- Calculates total token count using `tiktoken`
- Compares against model context sizes (4k, 8k, 32k)
- Renders an interactive token pressure report in the terminal

## Usage

```bash
pip install -r requirements.txt
python sandbox.py test_prompt.txt
```

## Output Example

```
Total Tokens: 1347

Token Pressure Report
---------------------
Model Context   | Status
4096 tokens     | Safe
8192 tokens     | Safe
32768 tokens    | Safe
```

## Notes

- Uses GPT-3.5/4 tokenizer via `tiktoken`
- Drop in your own `.txt` files to test prompt size
