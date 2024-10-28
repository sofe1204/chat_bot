from random import choice, randint

def get_response(user_input: str) -> str:
    lowered = user_input.lower()

    if lowered == "":
        return "Well, you're silent..."
    elif 'hello' in lowered:
        return choice(["Hello there!", "Hey!", "Hi! How's it going?"])
    elif 'how are you' in lowered:
        return choice(["Good, thanks!", "Doing well, how about you?", "I’m here and ready to chat!"])
    elif 'bye' in lowered:
        return choice(["See you!", "Goodbye!", "Catch you later!"])
    elif 'roll dice' in lowered:
        return f"You rolled: {randint(1, 6)}"
    elif 'flip a coin' in lowered:
        return f"The coin landed on: {'Heads' if randint(0, 1) == 0 else 'Tails'}"
    elif 'tell me a joke' in lowered:
        return choice([
            "Why did the computer go to the doctor? It had a virus!",
            "What’s a computer’s least favorite food? Spam.",
            "Why do Java developers wear glasses? Because they don’t see sharp!"
        ])
    elif 'what is your name' in lowered:
        return "I'm your friendly Discord bot!"
    elif 'favorite color' in lowered:
        return choice(["Blue!", "I like green!", "Red is pretty cool too!", "I'd say... rainbow!"])
    elif 'motivate me' in lowered:
        return choice([
            "You’ve got this!",
            "Keep going, you’re doing amazing!",
            "Don’t give up now. You’re closer than you think!"
        ])
    elif 'who created you' in lowered:
        return "I was created by an awesome programmer!"
    elif 'weather' in lowered:
        return "I’m not great with weather predictions, but I can say it’s a good day to code!"
    elif 'what can you do' in lowered:
        return "I can chat, tell jokes, roll dice, flip coins, and keep you company!"
    elif 'help' in lowered:
        return "Here are some things you can ask me: 'tell me a joke', 'roll dice', 'flip a coin', 'motivate me', or just say 'hello'!"
    elif 'thank you' in lowered:
        return choice(["You're welcome!", "No problem!", "Happy to help!"])
    
    
    elif 'favorite programming language' in lowered:
        return choice(["I’m a fan of Python!", "JavaScript is pretty versatile!", "I’d say… C++! It’s a classic."])
    elif 'what is programming' in lowered:
        return "Programming is the process of creating instructions for computers to execute. It’s like teaching computers how to solve problems!"
    elif 'recommend a programming language' in lowered:
        return choice([
            "Python is great for beginners!", 
            "JavaScript is useful if you want to build for the web.", 
            "Java is solid for many applications, especially if you're into Android development."
        ])
    elif 'what is an algorithm' in lowered:
        return "An algorithm is a set of instructions designed to perform a specific task. It’s a way to solve problems efficiently!"
    elif 'difference between frontend and backend' in lowered:
        return "Frontend development focuses on what users see and interact with, while backend handles the data, server, and business logic behind the scenes."
    elif 'what is ai' in lowered:
        return "AI, or Artificial Intelligence, is the simulation of human intelligence in machines designed to think and learn like humans!"
    elif 'data structure' in lowered:
        return "Data structures are ways of organizing and storing data so that we can access and modify it efficiently. Examples include arrays, lists, and trees."
    elif 'design patterns' in lowered:
        return "Design patterns are reusable solutions to common software design problems. They help make code more flexible and maintainable."
    elif 'what is debugging' in lowered:
        return "Debugging is the process of identifying and fixing errors or 'bugs' in your code. It’s an essential part of programming!"
    elif 'explain object oriented programming' in lowered or 'oop' in lowered:
        return "Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects, which contain data and methods. It’s used for structuring programs and making code reusable."
    elif 'recommend a cs book' in lowered:
        return choice([
            "Try 'Clean Code' by Robert C. Martin!", 
            "'The Pragmatic Programmer' is also a great read.", 
            "'Introduction to Algorithms' is a must-read for deeper CS knowledge!"
        ])
    elif 'fun fact about programming' in lowered:
        return choice([
            "The first computer programmer was Ada Lovelace in the 1800s!",
            "The first version of Python was released in 1991 by Guido van Rossum.",
            "The term 'bug' in programming was popularized by an actual moth found in a computer!"
        ])
    else:
        return choice(["I'm not sure about that.", "Try asking something else!", "Hmm... I don't quite get it."])
