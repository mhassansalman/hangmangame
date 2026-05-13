import scores

def hangmanpatterns():
    hangmanPattern = {
        0: (" _____   ", "|     |  ", "|        ", "|        ", "|        "),
        1: (" _____   ", "|     |  ", "|     O  ", "|        ", "|        "),
        2: (" _____   ", "|     |  ", "|     O  ", "|     |  ", "|        "),
        3: (" _____   ", "|     |  ", "|     O  ", "|    /|  ", "|        "),
        4: (" _____   ", "|     |  ", "|     O  ", "|    /|\\", "|        "),
        5: (" _____   ", "|     |  ", "|     O  ", "|    /|\\", "|    /   "),
        6: (" _____   ", "|     |  ", "|     O  ", "|    /|\\", "|    / \\"),
    }
    return hangmanPattern

def listselection():
    import random
    import lists
    all_lists = [lists.list_veg, lists.list_fruit, lists.list_sports]
    random_list = random.choice(all_lists)
    if random_list == lists.list_veg:
        hint1 = "Vegetable name"
    elif random_list == lists.list_fruit:
        hint1 = "Fruit name"
    elif random_list == lists.list_sports:
        hint1 = "Sports name"
    word = random.choice(random_list)
    return word, hint1

def displayman(wrongcount):
    for line in hangmanpatterns()[wrongcount]:
        print(line)
    print("==" * 5)

def saveplayerdata():
    with open("scores.py", "w") as f:
        f.write(f"player_data = {scores.player_data}")

def hangmangame(player_name):
    word, hint1 = listselection()
    wordlettersset = set(word)
    guessedlettersset = set()
    wrongguessesset = set()
    wrongcount = 0

    # Initialize player if new
    if player_name not in scores.player_data:
        scores.player_data[player_name] = {"wins": 0, "losses": 0, "total_games": 0}

    print(f"\nWelcome, {player_name}!")
    print(f"Stats: Wins = {scores.player_data[player_name]['wins']}, "
          f"Losses = {scores.player_data[player_name]['losses']}, "
          f"Total Games = {scores.player_data[player_name]['total_games']}")

    displayman(wrongcount)
    print("Hint:", hint1)
    current_display = ["_"] * len(word)
    print(" ".join(current_display))

    while True:
        # Input validation
        while True:
            print("-------------------------------------------------------")
            guess = input("Enter a single letter: ").strip().lower()
            if len(guess) == 1 and guess.isalpha():
                break
            print("Invalid input. Please enter a single letter.")

        if guess in wordlettersset:
            print("Right guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    current_display[i] = guess
            if guess in guessedlettersset:
                print("You already guessed that letter. Try again.")
            else:
                guessedlettersset.add(guess)
        else:
            print("Wrong guess!")
            if guess in wrongguessesset:
                print("You already attempted that wrong letter. Try again.")
            else:
                wrongguessesset.add(guess)
                wrongcount += 1
                print(f"Wrong Attempts: {wrongcount}")

        displayman(wrongcount)
        print(" ".join(current_display))

        if "_" not in current_display:
            print("Congratulations! You Won!")
            scores.player_data[player_name]["wins"] += 1
            break
        elif wrongcount >= 6:
            print(f"Game Over! The correct word was: {word}")
            scores.player_data[player_name]["losses"] += 1
            break

    scores.player_data[player_name]["total_games"] += 1
    saveplayerdata()

def play_again(player_name):
    while True:
        choice = input("Do you want to play again? (y/n): ").strip().lower()
        if choice == 'y':
            hangmangame(player_name)
        elif choice == 'n':
            print(f"\nThanks for playing! Goodbye, {player_name}!")
            print(f"Final Stats: Wins = {scores.player_data[player_name]['wins']}, "
                  f"Losses = {scores.player_data[player_name]['losses']}, "
                  f"Total Games = {scores.player_data[player_name]['total_games']}")
            break
        else:
            print("Invalid input. Please enter 'y' for Yes or 'n' for No.")

# --- Entry Point ---
player_name = input("Enter your first name: ").strip()
hangmangame(player_name)
play_again(player_name)
