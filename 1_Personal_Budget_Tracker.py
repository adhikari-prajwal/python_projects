names = []
amounts = []
categories = []

def add_expense():
    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a number.")
        return

    category = input("Enter category: ")

    if name == "":
        print("Expense name cannot be empty.")
    elif amount <= 0:
        print("Amount must be greater than 0.")
    else:
        names.append(name)
        amounts.append(amount)
        categories.append(category)
        print("Expense added.")

def show_expenses():
    if len(names) == 0:
        print("No expenses found.")
        return

    total = 0

    for i in range(len(names)):
        print(i + 1, names[i], "- Rs.", amounts[i], "-", categories[i])
        total = total + amounts[i]

    print("Total spent: Rs.", total)

def find_category():
    category = input("Enter category to search: ")
    found = False

    for i in range(len(names)):
        if categories[i].lower() == category.lower():
            print(names[i], "- Rs.", amounts[i])
            found = True

    if found == False:
        print("No expense found in this category.")

def check_budget():
    try:
        budget = float(input("Enter your budget: "))
    except ValueError:
        print("Please enter a number.")
        return

    total = 0

    for amount in amounts:
        total = total + amount

    remaining = budget - total
    print("Budget: Rs.", budget)
    print("Spent: Rs.", total)
    print("Remaining: Rs.", remaining)

    if remaining < 0:
        print("You have crossed your budget.")
    else:
        print("You are within your budget.")

def delete_expense():
    show_expenses()

    if len(names) == 0:
        return

    try:
        number = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Please enter a whole number.")
        return

    if number >= 1 and number <= len(names):
        position = number - 1
        names.pop(position)
        amounts.pop(position)
        categories.pop(position)
        print("Expense deleted.")
    else:
        print("Invalid expense number.")

def main():
    while True:
        print("\n--- PERSONAL BUDGET TRACKER ---")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Search category")
        print("4. Check budget")
        print("5. Delete expense")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            find_category()
        elif choice == "4":
            check_budget()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

main()
