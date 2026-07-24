# Basic Rule-Based Chatbot

A simple text-based chatbot built in Python that responds to user input using predefined rules.

## Description

The chatbot reads user input from the console and matches it against sets of known phrases (like greetings, "how are you", thanks, and goodbyes). Based on the match, it returns an appropriate predefined reply. If the input doesn't match any known pattern, it falls back to a generic response. The conversation continues in a loop until the user says a goodbye phrase (e.g., "bye", "exit", "quit").

## Features

- Recognizes common conversational inputs: greetings, "how are you", asking the bot's name, thanks, and goodbyes
- Randomized replies within each category for more natural-feeling conversation
- Graceful fallback response for unrecognized input
- Handles empty input without crashing
- Runs in a continuous loop until the user ends the conversation

## Concepts Demonstrated

- `if-elif` statements — matching user input to the correct response category
- Functions — `get_response()`, `is_goodbye()`, and `chat()` separate logic cleanly
- Loops — `while True` loop keeps the conversation going until exit
- Input/output — reading from the console with `input()` and printing responses

## How to Run

1. Make sure Python 3 is installed on your machine.
2. Save `chatbot.py` to a folder.
3. Open a terminal in that folder and run:

   ```
   python chatbot.py
   ```

4. Type messages like `hello`, `how are you`, or `bye` and press Enter.

## Example Conversation

```
Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.

You: hello
Chatbot: Hi!

You: how are you
Chatbot: I'm fine, thanks!

You: thanks
Chatbot: You're welcome!

You: bye
Chatbot: Goodbye!
```

## File Structure

```
chatbot.py    # Main chatbot script
README.md     # Project documentation
```

## Possible Future Improvements

- Use more flexible matching (e.g., check if a keyword appears anywhere in the sentence, not just exact matches)
- Add more intents and responses (jokes, weather, small talk)
- Store conversation history and use it for context-aware replies
- Build a GUI version using Tkinter or a web version using Flask

## Author

Submitted as part of an internship assignment.
