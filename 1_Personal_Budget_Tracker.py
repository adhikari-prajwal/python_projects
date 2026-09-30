

expenses = []


def add_expense():
    print("\n--- Add Expense ---")
    name = input("Enter expense name: ").strip()

    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    category = input("Enter category (Food/Travel/Bills/Other): ").strip()

    expenses.append({
        "name": name,
        "amount": amount,
        "category": category if category else "Other"
    })

    print("Expense added successfully.")


def view_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses have been added yet.")
        return

    total = 0

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - Rs. {expense['amount']:.2f} "
              f"({expense['category']})")
        total += expense["amount"]

    print(f"Total spent: Rs. {total:.2f}")


def category_summary():
    print("\n--- Category Summary ---")

    if not expenses:
        print("No expenses available.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        categories[category] = categories.get(category, 0) + expense["amount"]

    for category, amount in categories.items():
        print(f"{category}: Rs. {amount:.2f}")


def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        number = int(input("Enter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        removed = expenses.pop(number - 1)
        print(f"{removed['name']} was deleted.")

    except ValueError:
        print("Please enter a whole number.")


def budget_summary():
    print("\n--- Budget Summary ---")

    try:
        budget = float(input("Enter your monthly budget: "))

        if budget <= 0:
            print("Budget must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    total = sum(expense["amount"] for expense in expenses)
    remaining = budget - total

    print(f"Budget: Rs. {budget:.2f}")
    print(f"Spent: Rs. {total:.2f}")
    print(f"Remaining: Rs. {remaining:.2f}")

    if remaining < 0:
        print("Warning: You have exceeded your budget!")
    else:
        print("You are within your budget.")


def main():
    while True:
        print("\n===== PERSONAL BUDGET TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Category summary")
        print("4. Delete expense")
        print("5. Check budget")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            budget_summary()
        elif choice == "6":
            print("Thank you for using Personal Budget Tracker.")
            break
        else:
            print("Invalid choice. Please choose 1 to 6.")


main()
