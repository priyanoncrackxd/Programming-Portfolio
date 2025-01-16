import random
import json
import os

def load_config():
    try:
        with open("luffy.json", "r") as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print("Error: luffy.json file not found!")
        exit(1)
    except json.JSONDecodeError:
        print("Error: luffy.json is not a valid JSON file!")
        exit(1)

def random_agent(agent_names):
    return random.choice(agent_names)

def responses(question, user_name, replies, random_responses):
    for keyword, response in replies.items():
        if keyword in question.lower():
            return response
    return random.choice(random_responses)

def tell_joke(jokes):
    joke = random.choice(jokes)
    user_response = input("Would you like to hear a joke/pun before you leave? (yes/no): ").lower()
    
    if user_response in ['yes', 'y']:
        print(f"Here's a joke/pun: {joke}")
    elif user_response in ['no', 'n']:
        print("Okay, see you again!")
    else: 
        print("Please enter a valid input next time. Goodbye!")


def start_chat():
    config = load_config()
    
    print("Welcome to the Chatbot for the University of Poppleton!")
    user_name = input("Please enter your name: ")
    agent_name = random_agent(config['agent_names'])
    print(f"Hello {user_name}, I'm  your assistant {agent_name}! How can I assist you?")
    
    while True:
        user_question = input(f"{user_name}: ")
        
        if user_question.lower() in ['quit', 'exit', 'bye', 'byebye', 'goodbye']:
            print(f"{agent_name}: Goodbye, {user_name}! Have a great day!")
            tell_joke(config['jokes'])
            break

        if random.random()< 0.1:
            print("You have been disconnected randomly! Please try using the chatbot again ")
            break
            
        response = responses(user_question, user_name, config['replies'], config['random_responses'])
        print(f"{agent_name}: {response}")

# this starts the code
if __name__ == "__main__":
    start_chat()
