import random

words = ["computer", "python", "school", "keyboard", "internet",
         "science", "program", "function"]

score = 0

def scramble(word):
    letters = list(word)
    random.shuffle(letters)
    result = ""

    for letter in letters:
        result = result + letter

    return result

def play_game():
    global score

    word = random.choice(words)
    mixed = scramble(word)

    print("\nScrambled word:", mixed)

    for attempt in range(3):
        answer = input("Guess the word: ").lower()

        if answer == word:
            print("Correct!")
            score = score + (3 - attempt)
            return
        else:
            print("Wrong guess.")

    print("The correct word was:", word)

def add_word():
    word = input("Enter a new word: ").lower()

    if word == "":
        print("Word cannot be empty.")
    elif word in words:
        print("Word already exists.")
    else:
        words.append(word)
        print("Word added.")

def show_words():
    print("\nWord list:")

    for word in words:
        print("-", word)

def main():
    while True:
        print("\n--- WORD SCRAMBLE GAME ---")
        print("1. Play game")
        print("2. Add word")
        print("3. Show words")
        print("4. Show score")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            add_word()
        elif choice == "3":
            show_words()
        elif choice == "4":
            print("Your score:", score)
        elif choice == "5":
            print("Game ended.")
            break
        else:
            print("Invalid choice.")

main()
