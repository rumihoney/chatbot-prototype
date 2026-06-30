'''
Talk to Me

Rule-Based Chatbot Prototype for LING 498 – Computational Methods in Linguistics

Author: Roumaissaa Lassal 

Description:
The chatbot performs lexical preprocessing using NLTK,
detects conversational intents through keyword matching,
stores simple conversational memory, and records
conversation logs.
'''

import sys
import random                                                         # randomly selects a response to reduce repetition.
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download these if needed
# nltk.download("punkt")
# nltk.download("wordnet")
# nltk.download("omw-1.4")

from experiments import existential_scenario                          # existential scenario dialogue  
from experiments import therapist_chat                                # therapist chat dialogue


# ======================================================
# Memory storage
# ======================================================
memory = {}                                                           # dictionary used to store data learned from the convo
history = []                                                          # list that keeps track of the full conversation log


# ======================================================
# Lemmatizer: reducing words to base form
# ======================================================

lemmatizer = WordNetLemmatizer()


# ======================================================
# Error minimization function
# ======================================================
def get_int(prompt):
    while True:                                                       # infinite loop until valid input is given
        text = input(prompt).strip().lower()                          # get user input and remove extra spaces
        
        if text in ["exit", "quit", "bye"]:                           # check for exit commands
            print("Goodbye! Ending conversation.")                    # exit the program if user wants to end the conversation whenever
            sys.exit()
            
        if text.isdigit():                                            # check if the input contains only digits
            return int(text)                                          # convert to integer and return       
        print("Please type a number.")                                # if input is not a number, show error message


# ======================================================
# Intent detector and response generator
# ======================================================
intents = {
    "greet": {
        "trigger": ["hello", "hi", "hey", "what's up"], 
        "responses": ["Hello!", "Hi there!"]
        },
    "goodbye": {
        "trigger": ["bye", "see you", "exit"], 
        "responses": ["Goodbye!", "See you later!"]
        },
    "thanks": {
        "trigger": ["thanks", "thank you", "thx"], 
        "responses": ["You're welcome!", "Glad to help!"]
        }
}

# Preprocess user input through tokenization and lemmatization
def preprocess_text(text):
    text = text.lower().strip()
    tokens = word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha()]
    return lemmas
# "Thanks!" becomes "thank"
# "dogs" becomes "dog"

# Function to find intent
def find_intent(user_input):
    user_lemmas = preprocess_text(user_input)
    
    for intent_name, data in intents.items():
        for phrase in data["trigger"]:
            trigger_lemmas = preprocess_text(phrase)
            
            if all(word in user_lemmas for word in trigger_lemmas):
                return intent_name
            
    return None

# Generate a chatbot response from the detected intent
def chatbot_response(user_input):
    intent_name = find_intent(user_input)                             # detect intent
    if intent_name is not None:
        return random.choice(intents[intent_name]["responses"])       # pick a random response 
    return "I'm not sure how to respond to that."                     # fallback when no intent matches


# ======================================================
# Greeting phase & intent detection
# ======================================================
user_input = input('Hello, I am Rumi\'s chatbot! "Talk to Me",  Say something to start (hi/thanks/bye): ')

intent = find_intent(user_input)

if intent == "goodbye":
    print(random.choice(intents["goodbye"]["responses"]))
    sys.exit()

elif intent == "thanks":
    print(random.choice(intents["thanks"]["responses"]))

elif intent == "greet":
    print("Hello there! Let's get to know each other a bit more.")

else:
    print("I'm not sure how to respond to that.")
    

# ======================================================
# Main conversation loop
# ======================================================
name = ""
while not name.strip():                                               # using strip method to ensure name is not empty or spaces
    name = input("What is your name? ")           
    
    if name.lower() in ["exit", "quit", "bye"]:                       # check for exit commands
        print("Goodbye! Ending conversation.")                        # Exit the program if user wants to end the conversation whenever
        sys.exit()
        
    if not name.strip():                                              # if entry still empty it will prompt the user to enter it again
        print("Please enter your name.")
        
memory["name"] = name                                                 # storing name in memory
print(f"Nice to meet you {name}")                                     # if name input entered, print this output

history.append(("user", name))                                        # log interaction
history.append(("bot", f"Nice to meet you {name}!"))


# ======================================================
# Age interaction
# ======================================================
age = get_int("How old are you? ")                                    # continues asking until the user enters a valid integer.
                                                                                                                              
if age > 25:
    response = "Congratulations, your frontal lobe is fully developed!"
elif age < 18:
    response = "You are just a baby!"
else:
    response = f'So you are {age} years old!'   
print(response)                                                       # output

history.append(("user", str(age)))
history.append(("bot", response))

memory["age"] = age                                                   # storing age in memory


# ======================================================
# Colour interaction
# ======================================================
colour = input("What is your favourite colour? ").strip().lower()

# Dictionary mapping colours to responses
colour_responses = {
    "blue": "blue is cute",
    "red": "ew",
    "green": "It's giving Hobbit vibes",
    "purple": "Purple is my favourite colour too!"
}

if colour.isdigit():
    print("Please type a colour, not a number")
else:
    memory["colour"] = colour

response = colour_responses.get(colour, "Okay weird")                 # retrieve colour from dictionary or use default response
print(response)

history.append(("user", colour))
history.append(("bot", response))


# ======================================================
# Number interaction
# ======================================================
number = get_int("Give me a number between 1 and 10: ")

if number == 7:
    response = "Wow, lucky number 7!"
elif number == 3 or number == 5:
    response = "NUMBERS!"
elif number > 10:
    response = "Sneaky little bastard! That's not between 1 and 10!"
else:
    response = "Meh, that's an okay number I guess."
print(response)

history.append(("user", str(number)))
history.append(("bot", response))


# ======================================================
# Dialogue experiments
# ======================================================

# Optional dialogue experiments developed during testing.
# These can be enabled to explore alternative conversation flows.

# existential_scenario(get_int, history)
# therapist_chat(history)


# ======================================================
# Free chat mode
# ======================================================

def free_chat_mode():
    print("\n--- Free chat mode (type 'exit' to stop) ---")

    while True:
        user_input = input("> ").strip()
        reply = chatbot_response(user_input)

        history.append(("user", user_input))
        history.append(("bot", reply))

        print(reply)

        if find_intent(user_input) == "goodbye":
            break
        

# ======================================================
# Program termination
# ======================================================

def save_conversation(filename="conversation_logs.txt"):
# Save the conversation history to a text file.
    with open(filename, "w") as file:
        for speaker, text in history:
            file.write(f"{speaker.upper()}: {text}\n")


free_chat_mode()
save_conversation()

print("\nConversation saved to conversation_logs.txt.")
