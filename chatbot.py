print("🤖 Welcome to StudentBuddy!")
print("I am a simple rule-based chatbot.")
print("You can ask me about Python, AI, studying, programming, college, or ask for a joke.")
print("Type 'bye' whenever you want to exit.\n")


while True:
    user_input = input("You: ").lower().strip()

    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        print("Bot: Hey! 👋 Nice to meet you!")

    # How are you
    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking 😊")

    # Bot's name
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I'm StudentBuddy, your simple rule-based study assistant. 🤖")

    # Python
    elif "python" in user_input:
        print("Bot: Python is a popular programming language used in AI, automation, web development, and many other fields. 🐍")

    # Artificial Intelligence
    elif "artificial intelligence" in user_input or user_input == "ai":
        print("Bot: Artificial Intelligence allows computers to perform tasks that normally require human intelligence. 🤖")

    # Studying
    elif any(word in user_input for word in ["study", "studying", "exam", "exams"]):
        print("Bot: Try studying in small focused sessions, take short breaks, and practice what you learn. 📚")

    # Programming
    elif any(word in user_input for word in ["programming", "coding", "code"]):
        print("Bot: Programming means giving instructions to a computer to solve a problem or perform a task. 💻")

    # College
    elif "college" in user_input:
        print("Bot: College is a great place to learn, experiment, meet people, and build projects! 🎓")

    # Joke
    elif "joke" in user_input:
        print("Bot: Why did the programmer quit his job? Because he didn't get arrays! 😂")

    # Help
    elif "help" in user_input:
        print("Bot: You can ask me about Python, AI, studying, programming, college, or ask for a joke.")

    # Goodbye
    elif any(word in user_input for word in ["bye", "exit", "quit"]):
        print("Bot: Goodbye! 👋 Keep learning and building!")
        break

    # Unknown input
    else:
        print("Bot: Hmm 🤔 I don't know how to answer that yet. Try asking about Python, AI, studying, or programming.")