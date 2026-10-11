# Local AI Chat Demo

A small Python script that sends a chat completion request to a locally running, OpenAI-compatible model server. It is currently configured to use Ollama at `http://127.0.0.1:11434/v1` with the `Qwen3:4b` model.

## Current project status

- `simple_ai.py` creates an OpenAI Python client pointed at the local server.
- It sends a chat request with a system message and prints the model's response.
- The user message is currently commented out, so add or uncomment one in `messages` to ask the model something.
- The `openai` Python package is installed in the project's `.venv` and its import was verified.

## Requirements

- Python 3.12 (the current virtual environment uses Python 3.12)
- Ollama installed and running locally
- The `Qwen3:4b` model available in Ollama

## Setup

From the project directory, activate the virtual environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the Python dependency if needed:

```powershell
python -m pip install openai
```

Make sure Ollama is running and the model is available. If needed, download the model with:

```powershell
ollama pull Qwen3:4b
```

Run the script:

```powershell
python .\simple_ai.py
```

The script prints the response from the local model. It does not require an OpenAI API key; the configured API key is a placeholder for the local server.
