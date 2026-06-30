# Experimental dialogues: Testing branching dialogue.


# -----------------------------------------------------
# Existential scenario
# -----------------------------------------------------
def existential_scenario(get_int, history):
    choice = get_int(
        "\nOH NOOOOO, You have just died! Type a number between 1 and 3:\n"
    )

    if choice == 1:
        response = "Nothing has happened, you are still dead.\nGame Over"

    elif choice == 2:
        response = "JESUS! You have been resurrected"

    elif choice > 3:
        answer = input(
            "You have just entered the vortex. Would you like to proceed? (yes/no): "
        ).strip().lower()

        if answer == "yes":
            response = "Congratulations, you have won a cookie"
        elif answer == "no":
            response = "You have fallen into the death abyss.\nGame Over"
        else:
            response = "The universe does not understand your answer."

    else:
        response = "What the hell"

    print(response)

    history.append(("user", str(choice)))
    history.append(("bot", response))
    
    
# -----------------------------------------------------
# Therapist
# -----------------------------------------------------

# counseling function
def therapist_chat(history):
    print("What brings you here today.")
    
    feeling = input("How are you feeling today? ").strip().lower()
    
    history.append(("user", feeling))
    
    if "sad" in feeling:
        response = "I'm sorry you're feeling sad. Would you like to talk about what happened?"
    elif "happy" in feeling:
        response = "That's wonderful to news! What seems to be the source of this joy?"
    elif "angry" in feeling:
        response = "It sounds like something has been frustrating you. What happened?"
    elif "anxious" in feeling or "worried" in feeling:
        response = "That sounds difficult. What's been on your mind lately?"
    else:
        response = "Tell me a little more."

    print(response)
    history.append(("bot", response))

    follow_up = input("> ")
    history.append(("user", follow_up))

    print("Thank you for sharing that with me.")
    history.append(("bot", "Thank you for sharing that with me."))