# AI Chat Bot

A Python-based conversational AI chatbot powered by the Groq API (LLaMA 3.3 70B). Runs as a CLI app with persistent session logging and a modular codebase built for easy extension.

---

## Features

- Multi-turn conversation memory with a rolling context window
- Powered by LLaMA 3.3 70B via Groq's free API — fast and accurate
- Automatic session logging to dated files in `logs/`
- Clean modular architecture — API client, memory, and logger are fully separated
- `.env` based config — no hardcoded secrets

---

## Tech Stack

- Python 3.10+
- [Groq API](https://console.groq.com) (LLaMA 3.3 70B)
- python-dotenv
- Flask *(web interface — coming soon)*

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/sxhumr/ai-chat-bot.git
cd ai-chat-bot
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\Activate.ps1

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key
Create a `.env` file in the root folder:
GROQ_API_KEY=your-groq-api-key-here
Get a free key at [console.groq.com](https://console.groq.com).

### 5. Run the chatbot
```bash
python main.py
```

Type `clear` to reset the conversation, `quit` to exit.

---

## Project Structure
ai-chat-bot/
├── chatbot/
│   ├── client.py       # Groq API wrapper
│   ├── memory.py       # Conversation history manager
│   └── logger.py       # Session log writer
├── web/
│   ├── app.py          # Flask web server (in progress)
│   └── templates/
│       └── index.html  # Browser chat UI (in progress)
├── logs/               # Auto-generated session logs
├── main.py             # CLI entry point
├── .env.example        # API key template
├── requirements.txt
└── README.md

---

## Roadmap

Features planned for future versions:

- **Web UI** — Browser-based chat interface using Flask, with a clean bubble chat layout and real-time streaming responses
- **Streaming responses** — Print the assistant's reply word by word as it generates, instead of waiting for the full response
- **Persona system** — Launch the bot with a custom personality via a `--persona` flag (e.g. `python main.py --persona tutor`)
- **Long-term memory** — Store key facts from past sessions in a local JSON or SQLite database so the bot remembers you across restarts
- **Voice input / output** — Integrate `speech_recognition` and `pyttsx3` so you can speak to the bot and hear it respond
- **RAG (Retrieval-Augmented Generation)** — Feed the bot your own documents (PDFs, notes) and let it answer questions about them using vector search
- **Multi-model support** — Switch between Groq, OpenAI, and local Ollama models from a config file without changing any code
- **Web search tool** — Give the bot real-time internet access using the Tavily or SerpAPI search APIs
