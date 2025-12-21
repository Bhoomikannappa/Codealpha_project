from datetime import datetime
import random

name  = ""
bot_name = "ChattyBhoo"

responses = {
        "greetings" : ["Hello there! 😊", "Hi! Nice to see you! 👋"],
        "how_are_you" : ["I'm doing great, thanks! 🥰", "Feeling fantastic today! 🌟"],
        "farewells" : ["Goodbye! Hope to see you again! 👋", "Take care! 😊"]
}

def get_response(key):
    """Get a random response from the available options"""
    return random.choice(responses.get(key, ["I'm here to help!"]))

def show_help():
    """Show what the bot can do"""
    help_text = f"""
┌─────────────────────────────────────┐
│   I can help you with:              │     
│   • Greetings and chat              │
│   • Tell time & date                │
│   • Remember your name              │
│   • Simple conversations            |
│                                     │
│   Try asking:                       │
│   • What can you do?                │
│   • How are you?                    │ 
│   • What's the time?                │
│   • Tell me a joke                  │
└─────────────────────────────────────┘
"""
    print(help_text)    

print(f"\n🤖 {bot_name}: Hi! I'm {bot_name}, your friendly chatbot!")
print("   Type 'help' to see what I can do, or 'bye' to exit.\n")

while True:
    user_input = input("You:").lower().strip()

    # Help command
    if user_input == "help":
        show_help()
        continue

    # Greetings
    if any(greet in user_input for greet in ["hello", "hi", "hey", "sup", "hola"]):
        print(f"🤖 {bot_name}: {get_response('greetings')}")
        if not name:
            print(f"   What's your name?")
        else:
            print(f"   Nice to see you again, {name}!")

    elif "how are you" in user_input:
        print(f"🤖 {bot_name}: {get_response('how_are_you')}")
        print(f"   How about you")

    elif  "good" in user_input or "great" in user_input or "awesome" in user_input:
        print(f"🤖 {bot_name}: that's great to hear")
    
    # User is feeling down
    elif "sad" in user_input or "bad" in user_input or "angry" in user_input:
        print(f"🤖 {bot_name}: Oh, I'm sorry to hear that. 😔")
        print("   Would you like to talk about it? Or I can tell you a joke! 😊")
            
    # About the bot
    elif any(phrase in user_input for phrase in ["who are you", "about you", "what are you"]):
        print(f"🤖 {bot_name}: I'm {bot_name}, a friendly chatbot! 🤖")
        print("   I'm here to chat, help with simple tasks, and keep you company!")
        print("   Type 'help' to see what I can do.")
    
    # Get/set name
    elif "my name is" in user_input:
        name = user_input.replace("my name is", "").strip().title()
        print(f"🤖 {bot_name}: Nice to meet you, {name}! 👋")
        print(f"   I'll remember that!")
    
    elif "what is my name" in user_input or "my name" == user_input:
        if name:
            print(f"🤖 {bot_name}: Your name is {name}! 😊")
        else:
            print(f"🤖 {bot_name}: I don't know your name yet. 😅")
            print("   What should I call you?")
    
    # Time
    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"🤖 {bot_name}: 🕒 The current time is {current_time}")
    
    # Date
    elif "date" in user_input:
        today = datetime.now().strftime("%B %d, %Y")
        print(f"🤖 {bot_name}: 📅 Today is {today}")
    
    # Joke request
    elif "joke" in user_input:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything! 🤣",
            "I told my computer I needed a break... now it won't stop sending me Kit-Kats! 🍫",
            "Why did the chatbot break up with the computer? It had too many connections! 💔"
        ]
        print(f"🤖 {bot_name}: {random.choice(jokes)}")
    
    # Thank you
    elif any(word in user_input for word in ["thank", "thanks"]):
        print(f"🤖 {bot_name}: You're welcome! 😊")
        if name:
            print(f"   Always happy to help, {name}!")
    
    # Goodbye
    elif any(word in user_input for word in ["bye", "goodbye", "exit", "quit"]):
        if name:
            print(f"🤖 {bot_name}: {get_response('farewells')}")
            print(f"   See you later, {name}! 👋")
        else:
            print(f"🤖 {bot_name}: {get_response('farewells')}")
        print("   [Chat ended]")
        break
    
    # Unknown input
    else:
        suggestions = ["Try asking about time or date", "Tell me your name!", "Ask me how I am!"]
        print(f"🤖 {bot_name}: Hmm, I'm not sure about that. 🤔")
        print(f"   💡 Try: '{random.choice(suggestions)}'")

        print(f"   Or type 'help' to see what I can do.")
