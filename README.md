# Rule Based ChatBot

A simple Python chatbot that matches keywords in user input to pre-defined responses. Built as a beginner-friendly project to demonstrate dictionaries, string matching, and control flow in Python.

## Features

- Greets the user on startup
- Matches keywords/phrases in user input (case-insensitive) to canned responses
- Handles unrecognized input with a friendly fallback message
- Exits gracefully when the user types "bye"

## How It Works

The bot stores a dictionary of `keyword: response` pairs. For every message you type, it lowercases your input and checks whether any keyword appears as a substring. The first match found returns its associated response. If nothing matches, it returns a default "I don't understand" message.

## Requirements

- Python 3.7+

No external libraries are needed — it only uses built-in Python.

## Usage

Run the script from your terminal:

```bash
python chatbot_fixed.py
```

Then type a message when prompted:

```
Namaste! Welcome to Rule Based ChatBot
You can ask me basic questions, type 'bye' to exit.
Please enter your message: hello
Bot response:  hi , Welcome. How can I help you.?
Please enter your message: bye
Goodbye! Have a great day!
```

## Supported Keywords

| Keyword | Example Response |
|---|---|
| hello | Greets the user |
| how are you | Bot describes how it's doing |
| who are you | Bot introduces itself |
| motivate me | Gives a motivational message |
| happy | Encourages positivity |
| what is functions | Explains what a function is |
| what is class | Explains what a class is |
| bye | Ends the conversation |

## Known Limitations

- **Substring matching, not word matching**: a keyword can match inside a longer word (e.g., "hi" inside "history"). This is fine for casual use but can occasionally cause false matches.
- **Single match per message**: if a message contains more than one keyword, only the first one found (in dictionary order) triggers a response.
- **No context or memory**: each message is evaluated independently; the bot doesn't track conversation history.

## Possible Improvements

- Use word-boundary matching (regex) instead of plain substring checks
- Support multiple keyword matches in one message
- Add more keywords/responses or load them from an external file (JSON/CSV)
- Add simple NLP (e.g., fuzzy matching) for typo tolerance

## Author

Created by Harsh.
