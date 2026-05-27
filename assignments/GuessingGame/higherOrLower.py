import random

LEADERBOARD_PATH = r"C:\Users\tatum\OneDrive\Documents\intro to programming\IntroToProgramming\assignments\GuessingGame\leaderboard.txt"

def display_leaderboard():
    try:
        with open(LEADERBOARD_PATH, "r") as file:
            leaderboard = [line.split(",") for line in file.read().splitlines() if line.strip()]
        leaderboard.sort(key=lambda x: int(x[1]))
        print("\nLEADERBOARD:") 
        for i, entry in enumerate(leaderboard, 1):
            print(f"  {i}. {entry[0]}: {entry[1]} guesses")
    except FileNotFoundError:
        print("No scores yet!")

def play_game():
    while True:
        display_leaderboard()
        name = input("\nENTER YOUR NAME\n> ")
        target = random.randrange(1, 10)
        guess = 0
        num_guesses = 0

        while guess != target:
            guess = int(input("ENTER A NUMBER\n> "))
            num_guesses += 1
            if guess < target:
            
                print("LOW")
            elif guess > target:
                print("HIGH")

        print(f"CORRECT! THE NUMBER WAS {target}. You got it in {num_guesses} guesses!")

        with open(LEADERBOARD_PATH, "a") as file:
            file.write(f"\n{name},{num_guesses}")

        play_again = input("\nPLAY AGAIN?\n[y/n]\n> ")
        if play_again != "y":
            break

play_game()