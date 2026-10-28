# AI Personal Assistant

A clean, modern starter project for building your own personal AI assistant. Includes a CLI for quick notes and tasks, a FastAPI web interface, and a modular structure ready for LLM integration (OpenAI, Grok, local models, etc.).

Built with Python 3.11+, FastAPI, Typer, and best practices in mind.

## Features

- **CLI Interface**: Add notes, list tasks, mark complete, and get smart summaries (stubbed for AI).
- **Web API**: FastAPI endpoints for the same functionality + interactive docs.
- **Modular Design**: Services, models, and clear separation for easy extension.
- **Ready for AI**: Placeholder methods where you can plug in any LLM.
- **Tests**: Basic pytest coverage.
- **Clean Architecture**: Easy to grow into a full personal knowledge system.

## Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/aziz4rehman-hue/ai-personal-assistant.git
cd ai-personal-assistant
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the CLI

```bash
python -m ai_personal_assistant.cli --help
# Examples:
python -m ai_personal_assistant.cli note add "Meeting notes from today"
python -m ai_personal_assistant.cli task list
```

### 3. Run the Web API

```bash
uvicorn app:app --reload
# Open http://127.0.0.1:8000/docs
```

## Project Structure

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── app.py                  # FastAPI entrypoint
├── src/
│   └── ai_personal_assistant/
│       ├── __init__.py
│       ├── cli.py             # Typer CLI
│       ├── models.py          # Data models
│       └── services.py        # Business logic + AI stubs
└── tests/
    └── test_cli.py
```

## Extending with Real AI

In `services.py`, replace the `summarize` and `prioritize` methods with calls to your preferred LLM:

```python
# Example with OpenAI
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(...)
```

Or use Grok via xAI API, local Ollama, etc.

## License

MIT — feel free to use, modify, and build upon this.

---

Created as a solid foundation for personal AI tools. Happy building!
