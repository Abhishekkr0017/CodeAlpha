import random
GREETING_INPUTS = ["hello", "hi", "hey", "hola"]
GREETING_RESPONSES = ["Hi!", "Hello there!", "Hey! How can I help?"]

HOWAREYOU_INPUTS = ["how are you", "how are you doing", "how's it going"]
HOWAREYOU_RESPONSES = ["I'm fine, thanks!", "Doing great, thanks for asking!"]

NAME_INPUTS = ["what is your name", "who are you", "what's your name"]
NAME_RESPONSES = ["I'm a simple rule-based chatbot.", "You can call me ChatBot."]

THANKS_INPUTS = ["thank you", "thanks"]
THANKS_RESPONSES = ["You're welcome!", "No problem at all!"]

BYE_INPUTS = ["bye", "goodbye", "see you", "exit", "quit"]
BYE_RESPONSES = ["Goodbye!", "See you later!", "Bye! Take care."]

DEFAULT_RESPONSES = [
    "Sorry, I didn't understand that.",
    "Could you rephrase that?",
    "I'm not sure how to respond to that.",
]


def get_response(user_input):
    """Return an appropriate response based on simple keyword matching."""
    text = user_input.lower().strip()

    if text in GREETING_INPUTS:
        return random.choice(GREETING_RESPONSES)
    elif text in HOWAREYOU_INPUTS:
        return random.choice(HOWAREYOU_RESPONSES)
    elif text in NAME_INPUTS:
        return random.choice(NAME_RESPONSES)
    elif text in THANKS_INPUTS:
        return random.choice(THANKS_RESPONSES)
    elif text in BYE_INPUTS:
        return random.choice(BYE_RESPONSES)
    else:
        return random.choice(DEFAULT_RESPONSES)


def is_goodbye(user_input):
    """Check whether the input should end the conversation."""
    return user_input.lower().strip() in BYE_INPUTS


def chat():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            print("Chatbot: Please type something.\n")
            continue

        response = get_response(user_input)
        print(f"Chatbot: {response}\n")

        if is_goodbye(user_input):
            break


if __name__ == "__main__":
    chat()
