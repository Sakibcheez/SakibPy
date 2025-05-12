import random
import re
import time

class SimpleBot:
    def __init__(self):
        self.name = "PyBot"
        # Dictionary of patterns and corresponding responses
        self.response_patterns = {
            r"hi|hello|hey": [
                f"Hello! I'm {self.name}. How can I help you today?",
                f"Hi there! Nice to meet you. I'm {self.name}.",
                "Hey! How are you doing today?"
            ],
            r"how are you": [
                "I'm doing well, thanks for asking!",
                "I'm good! How about you?",
                "All systems operational! How can I assist you?"
            ],
            r"your name|who are you": [
                f"I'm {self.name}, a simple chatbot.",
                f"My name is {self.name}. I'm here to chat!",
                f"I go by {self.name}. How can I help you?"
            ],
            r"bye|goodbye|exit": [
                "Goodbye! Have a great day!",
                "See you later!",
                "Bye! Come back soon!"
            ],
            r"thanks|thank you": [
                "You're welcome!",
                "Anytime!",
                "Happy to help!"
            ],
            r"weather": [
                "I'm not connected to real-time weather data, but I hope it's nice where you are!",
                "I can't check the weather, but maybe look outside?",
                "Sorry, I don't have access to weather information."
            ],
            r"joke|funny": [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What's a computer's favorite snack? Microchips!",
                "Why did the Python programmer need glasses? Because they couldn't C#!"
            ],
            r"time": [
                f"The current time is {time.strftime('%H:%M:%S')}.",
                f"It's currently {time.strftime('%I:%M %p')}.",
                "My clock says it's " + time.strftime("%H:%M") + " right now."
            ]
        }
        # Default responses for when no pattern matches
        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting! Tell me more about that.",
            "I don't have information about that yet.",
            "I'm still learning and don't know how to respond to that."
        ]
    
    def respond(self, user_input):
        # Convert to lowercase and remove extra whitespace
        processed_input = user_input.lower().strip()
        
        # Check if the input matches any of our patterns
        for pattern, responses in self.response_patterns.items():
            if re.search(pattern, processed_input):
                return random.choice(responses)
        
        # If no pattern matches, return a default response
        return random.choice(self.default_responses)
    
    def run(self):
        print(f"{self.name}: Hello! I'm {self.name}. Type 'bye' to exit.")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
                print(f"{self.name}: {self.respond(user_input)}")
                break
                
            response = self.respond(user_input)
            print(f"{self.name}: {response}")

# Create and run the bot
if __name__ == "__main__":
    bot = SimpleBot()
    bot.run()