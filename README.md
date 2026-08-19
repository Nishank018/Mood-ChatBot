# Mood-ChatBot 💬

Mood-ChatBot is a simple AI chat application where you can choose how the assistant responds. Built with Streamlit and Mistral AI, it keeps the conversation useful while changing the personality of each reply.

Choose from five moods:

- Neutral
- Funny
- Angry
- Sarcastic
- Formal

Changing the mood starts a fresh conversation so the assistant can keep a consistent tone.

## Features

- Clean browser-based chat interface
- Mood selector in the sidebar
- Conversation history for the current session
- One-click option to clear the chat
- Responses generated with Mistral's `mistral-small-latest` model

## Tech stack

- Python
- Streamlit
- LangChain
- Mistral AI
- python-dotenv

## Getting started

### 1. Clone the project

```bash
git clone <your-repository-url>
cd Mood-ChatBot
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install streamlit
```

### 4. Add your Mistral API key

Create a `.env` file in the project folder and add:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

You can get an API key from [Mistral AI](https://console.mistral.ai/).

### 5. Run the app

```bash
streamlit run MoodChatBot.py
```

Streamlit will open the app in your browser, usually at `http://localhost:8501`.

## How to use it

1. Select a mood from the sidebar.
2. Type a message into the chat box.
3. The assistant will reply in the selected style.
4. Use **Clear chat** whenever you want to begin again.

## Project structure

```text
Mood-ChatBot/
├── MoodChatBot.py      # Streamlit application
├── requirements.txt    # Python dependencies
├── .env                # Your Mistral API key (not committed)
└── README.md
```

## Notes

- Keep your `.env` file private and never commit API keys to GitHub.
- Mood changes intentionally clear existing messages to avoid mixing conversation styles.

## License

This project is for learning and personal use. Add a license file if you plan to share or distribute it.
