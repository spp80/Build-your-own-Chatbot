import nltk
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am doing well, thank you!', 'I\'m good, thanks for asking.']),
    (r'what is your name?', ['You can call me Chatbot.', 'My name is Chatbot.']),
    (r'quit', ['Bye, take care.', 'Goodbye!']),
]

# Create a Chatbot
def simple_chatbot():
    print("Hi! I'm Chatbot. How can I help you today?")

    # Create a Chat instance
    chatbot = Chat(patterns, reflections)

    # Start conversation
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    simple_chatbot()
