import random
from datetime import datetime

def get_time_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning! 🌞"
    elif hour < 18:
        return "Good afternoon! ☀️"
    else:
        return "Good evening! 🌙"

def chatbot():
    print("Zuzu 🤖: Hello! I’m your advanced chatbot. Type 'bye' to exit.")
    user_name = None

    # dictionary of keywords with lists of possible replies
    responses = {
        "hello": ["Hi!", "Hello there 👋", "Heyy! 🌸"],
        "hi": ["Hi!", "Hello there 👋", "Heyy! 🌸"],
        "how are you": ["I’m fine, Thanks! 🌼", "Doing great, how about you?", "All good here! 😄"],
        "bye": ["Goodbye! 👋", "See you later 🌸", "Bye bye, take care! 💖"],
        "your name": ["I’m Zuzu 🤖", "They call me Zuzu ✨", "I’m your chatbot buddy! 💬"],
        "what are you doing": ["I’m chatting with you! 💬", "Just waiting for your messages 👀", "Talking to my favorite human 🌼"],
        "sad": ["Oh no! 😢 Hope your day gets better 🌸", "I’m here for you! 💖", "Cheer up! Things will improve 🌼"]
    }

    conversation_log = []

    while True:
        user_input = input("You: ").lower()
        conversation_log.append(f"You: {user_input}")

        matched = False

        # check if user introduces their name
        if "my name is" in user_input:
            user_name = user_input.split("my name is")[-1].strip().capitalize()
            response = f"Nice to meet you, {user_name}! 🌸"
            print(f"Zuzu 🤖: {response}")
            conversation_log.append(f"Zuzu: {response}")
            matched = True

        # time-based greeting if user says hello/hi
        elif any(greet in user_input for greet in ["hello", "hi"]):
            response = f"{random.choice(responses['hello'])} {get_time_greeting()}"
            print(f"Zuzu 🤖: {response}")
            conversation_log.append(f"Zuzu: {response}")
            matched = True

        # check for other keywords
        else:
            for keyword, reply_list in responses.items():
                if keyword in user_input:
                    response = random.choice(reply_list)
                    # personalize with name if known
                    if user_name and "how are you" in keyword:
                        response = f"I’m fine, Thanks {user_name}! 🌼"
                    print(f"Zuzu 🤖: {response}")
                    conversation_log.append(f"Zuzu: {response}")
                    matched = True
                    if keyword == "bye":
                        # save chat log
                        with open("chat_log.txt", "a") as file:
                            for line in conversation_log:
                                file.write(line + "\n")
                            file.write("-"*30 + "\n")
                        return
                    break 

        if not matched:
            response = "Sorry, I don’t understand that yet."
            print(f"Zuzu 🤖: {response}")
            conversation_log.append(f"Zuzu: {response}")

chatbot()
