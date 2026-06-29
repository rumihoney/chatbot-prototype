# "Talk to Me" interactive little bot

import random                                                         # pick random response = less repetitive

# -----------------------------------------------------
# Memory storage
# -----------------------------------------------------
memory = {}                                                           # dictionary used to store data learned from the convo
history = []                                                          # list that keeps track of the full conversation log


# -----------------------------------------------------
# Error minimization function
# -----------------------------------------------------
def get_int(prompt):
    while True:                                                       # Infinite loop until valid input is given
        text = input(prompt).strip()                                  # Get user input and remove extra spaces
        if text.isdigit():                                            # Check if the input contains only digits
            return int(text)                                          # Convert to integer and return       
        print("Please type a number.")                                # if input is not a number, show error message


# -----------------------------------------------------
# Intent detector
# -----------------------------------------------------
intents = {
    "greet": {
        "trigger": ["hello", "hi", "hey"], 
        "responses": ["Hello! How can I assist you today?", "Hi there! How can I help?"]
        },
    "goodbye": {
        "trigger": ["bye", "see you", "exit"], 
        "responses": ["Goodbye! Have a great day!", "See you later!"]
        },
    "thanks": {
        "trigger": ["thanks", "thank you"], 
        "responses": ["You're welcome!", "Glad to help!"]
        }
}

# Function to find intent
def find_intent(user_input):
    for intent_name, data in intents.items():                         # Loop through each intent -> "greet", "goodbye", "thanks"
        for phrase in data["trigger"]:                                # Loop through each trigger phrase 
            if phrase in user_input.lower():                          # make phrase case-insensitive
                return intent_name                                    # return intent label e.g., "greet"
    return None                                                       # if nothing matches -> return None

# Function to convert user input -> bot reply
def chatbot_response(user_input):
    intent_name = find_intent(user_input)                             # detect intent
    if intent_name is not None:
        return random.choice(intents[intent_name]["responses"])       # pick a random response 
    return "I'm not sure how to respond to that."                     # fallback when no intent matches


# -----------------------------------------------------
# Greeting phase
# -----------------------------------------------------
user_input = input("Say something to start (hi/thanks/bye): ")
print(chatbot_response(user_input))

name = ""
while not name.strip():                                               # using strip method to ensure name is not empty or spaces
    name = input("What is your name? ")           
    if not name.strip():                                              # if entry still empty it will prompt the user to enter it again
        print("Please enter your name.")
        
memory["name"] = name                                                 # storing name in memory
print(f"Nice to meet you {name}")                                     # if name input entered, print this output

history.append(("user", name))                                        # log interaction
history.append(("bot", f"Nice to meet you {name}!"))


# -----------------------------------------------------
# Age interaction
# -----------------------------------------------------
age = get_int("How old are you? ")                                    # get_int() function from CS50 library to safely return user's input as an int 
                                                                      # function keeps asking the question until user gives a valid number
                                                         
memory["age"] = age                                                   # storing age in memory

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


# -----------------------------------------------------
# Colour interaction
# -----------------------------------------------------
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


# -----------------------------------------------------
# Number interaction
# -----------------------------------------------------
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


# -----------------------------------------------------
# Existential scenario
# -----------------------------------------------------
choice = get_int("\nOH NOOOOO, You have just died! Type a number between 1 and 3: \n")

if choice == 1:
    response = "Nothing has happened, you are still dead.\nGame Over"
    print(response) 
elif choice == 2:
    response = "JESUS! You have been resurrected"
    print(response)   
elif choice > 3:
    answer = input("You have just entered the vortex. Would you like to proceed? (yes/no): ").strip().lower()
    
    if answer == "yes":
        response = "Congratulations, you have won a cookie"
    elif answer == "no":
        response = "You have fallen into the death abyss.\nGame Over"
    else:
        response = "The universe does not understand your answer."
    print(response)
else:
    response = "What the hell"
    print(response)

history.append(("user", str(choice)))
history.append(("bot", response))


# -----------------------------------------------------
# Save conversation log
# -----------------------------------------------------
with open("conversation_logs.txt", "w") as file:
    # Write each turn to the file
    for speaker, text in history:
        file.write(f"{speaker.upper()}: {text}\n")
        
# need to review this section***


# -----------------------------------------------------
# Intent chat loop
# -----------------------------------------------------
print("\n--- Free chat mode (type 'exit' to stop) ---")

while True:
    user_input = input("> ")

    reply = chatbot_response(user_input)  # get a reply from your intent system
    print(reply)                          # show it

    # stop the loop if user intent is goodbye
    if find_intent(user_input) == "goodbye":
        break
