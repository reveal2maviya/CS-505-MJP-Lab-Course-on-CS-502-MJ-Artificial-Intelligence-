"""
Program: Simple Chatbot
Description: This program implements a basic chatbot that responds to common user greetings and farewells. Users can choose from a predefined list of inputs.

How to Run:
- On Ubuntu/Linux: Open the terminal and navigate to the directory containing this file. Use the command "python3 chatbot.py" to run the program.
- On Windows: Open a command prompt and navigate to the directory containing this file. Use the command "python chatbot.py" to run the program.
"""

# Common user inputs and their corresponding responses
responses = {
    "hi": "Hello there! How can I help you today?",
    "hello": "Hi! How can I assist you?",
    "hey": "Hey! What can I do for you?",
    "how are you": "I'm just a computer program, but I'm here to help you.",
    "bye": "Goodbye! Have a great day.",
    "exit": "Goodbye! If you have more questions, feel free to come back."
}

# Chatbot function
def chatbot(user_input):
    user_input = user_input.lower()  # Convert the input to lowercase for case-insensitive matching
    response = responses.get(user_input, "I'm not sure how to respond to that. Please choose from the predefined inputs. 'hi', 'hello', 'hey', 'how are you', 'bye', 'exit'")
    return response

# Main loop for user interaction
print("Simple Chatbot: Type 'bye' to exit")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye" or user_input.lower() == "exit":
        print("Simple Chatbot: Goodbye!")
        break
    response = chatbot(user_input)
    print("Simple Chatbot:", response)
