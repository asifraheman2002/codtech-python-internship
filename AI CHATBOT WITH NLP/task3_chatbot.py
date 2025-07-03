import random
import nltk
from nltk.chat.util import Chat, reflections

# Predefined patterns and responses
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["what is your name?", ["I am a chatbot built with Python."]],
    ["how are you?", ["I'm doing great, thanks!", "All good!"]],
    ["(.*) your creator?", ["I was created by a Python enthusiast!"]],
    ["bye|exit", ["Goodbye!", "See you soon!"]]
]

def chatbot():
    print("Hi! I am a chatbot. Type 'exit' to leave.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
