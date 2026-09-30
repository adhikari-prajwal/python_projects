import random

best_score = 0
games_played = 0

def play_game():
    global best_score
    global games_played

    number = random.randint(1, 50)
    attempts = 0

    print("\nI have chosen a number from 1 to 50.")
    print("You have 7 chances to guess it.")

    while attempts < 7:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if guess < 1 or guess > 50:
            print("Enter a number between 1 and 50.")
            continue

        attempts = attempts + 1

        if guess == number:
            print("Congratulations! You guessed correctly.")
            print("Attempts used:", attempts)

            score = 8 - attempts

            if score > best_score:
                best_score = score
                print("New best score!")

            games_played = games_played + 1
            return

        elif guess < number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

    print("You ran out of chances.")
    print("The number was:", number)
    games_played = games_played + 1

def show_hint():
    print("\nHint: Choose a number between 1 and 50.")
    print("If your guess is too low, try a higher number.")
    print("If your guess is too high, try a lower number.")

def main():
    while True:
        print("\n--- NUMBER GUESSING GAME ---")
        print("1. Play game")
        print("2. Show hint")
        print("3. Show best score")
        print("4. Show games played")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            show_hint()
        elif choice == "3":
            print("Best score:", best_score)
        elif choice == "4":
            print("Games played:", games_played)
        elif choice == "5":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice.")

main()