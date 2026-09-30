

import random

words = [
    "computer",
    "python",
    "keyboard",
    "internet",
    "school",
    "program",
    "function",
    "science"
]


def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)


def play_game():
    word = random.choice(words)
    scrambled = scramble_word(word)

    print("\nScrambled word:", scrambled)
    print("You have 3 attempts.")

    for attempt in range(1, 4):
        answer = input(f"Attempt {attempt}: ").strip().lower()

        if not answer:
            print("Please enter an answer.")
            continue

        if answer == word:
            points = 4 - attempt
            print(f"Correct! You earned {points} point(s).")
            return points

        if attempt < 3:
            print("Wrong answer. Try again.")
        else:
            print(f"Sorry! The correct word was '{word}'.")

    return 0


def add_word():
    word = input("Enter a new word: ").strip().lower()

    if not word.isalpha():
        print("Please enter letters only.")
        return

    if word in words:
        print("That word is already in the list.")
        return

    words.append(word)
    print("New word added successfully.")


def show_words():
    print("\n--- Word List ---")

    if not words:
        print("The word list is empty.")
        return

    for number, word in enumerate(words, start=1):
        print(f"{number}. {word}")


def main():
    score = 0
    games_played = 0

    while True:
        print("\n===== WORD SCRAMBLE GAME =====")
        print("1. Play game")
        print("2. Add a word")
        print("3. View word list")
        print("4. View score")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            score += play_game()
            games_played += 1
        elif choice == "2":
            add_word()
        elif choice == "3":
            show_words()
        elif choice == "4":
            print(f"Games played: {games_played}")
            print(f"Total score: {score}")
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please choose 1 to 5.")


main()
