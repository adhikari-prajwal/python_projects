

import random

best_score = None


def play_game():
    global best_score

    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 7

    print("\nI have selected a number from 1 to 50.")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 50:
                print("Please enter a number from 1 to 50.")
                continue

        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Correct! You guessed it in {attempts} attempt(s).")

            if best_score is None or attempts < best_score:
                best_score = attempts
                print("New best score!")

            return

        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")

        print(f"Attempts remaining: {max_attempts - attempts}")

    print(f"Game over! The number was {secret_number}.")


def show_hint():
    print("\nHint: The secret number is between 1 and 50.")
    print("Try to use the previous 'Too high' or 'Too low' messages.")


def main():
    games_played = 0

    while True:
        print("\n===== NUMBER GUESSING GAME =====")
        print("1. Play game")
        print("2. Get a hint")
        print("3. View best score")
        print("4. View games played")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            play_game()
            games_played += 1
        elif choice == "2":
            show_hint()
        elif choice == "3":
            if best_score is None:
                print("No score recorded yet.")
            else:
                print(f"Best score: {best_score} attempts")
        elif choice == "4":
            print(f"Games played: {games_played}")
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please choose 1 to 5.")


main()
