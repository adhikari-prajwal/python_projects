

shopping_list = []


def add_item():
    item = input("Enter grocery item: ").strip()

    if not item:
        print("Item name cannot be empty.")
        return

    if item.lower() in [x.lower() for x in shopping_list]:
        print("That item is already on the list.")
        return

    shopping_list.append(item)
    print("Item added.")


def view_items():
    print("\n--- Shopping List ---")

    if not shopping_list:
        print("Your shopping list is empty.")
        return

    for number, item in enumerate(shopping_list, start=1):
        print(f"{number}. {item}")


def remove_item():
    view_items()

    if not shopping_list:
        return

    try:
        number = int(input("Enter item number to remove: "))

        if number < 1 or number > len(shopping_list):
            print("Invalid item number.")
            return

        removed = shopping_list.pop(number - 1)
        print(f"{removed} removed from the list.")

    except ValueError:
        print("Please enter a whole number.")


def search_item():
    if not shopping_list:
        print("Your shopping list is empty.")
        return

    search = input("Enter item to search: ").strip().lower()

    for item in shopping_list:
        if item.lower() == search:
            print(f"{item} is on your shopping list.")
            return

    print("Item not found.")


def sort_items():
    if not shopping_list:
        print("Your shopping list is empty.")
        return

    shopping_list.sort()
    print("Shopping list sorted alphabetically.")


def clear_list():
    if not shopping_list:
        print("The list is already empty.")
        return

    confirm = input("Clear the entire list? (yes/no): ").strip().lower()

    if confirm == "yes":
        shopping_list.clear()
        print("Shopping list cleared.")
    else:
        print("List was not cleared.")


def main():
    while True:
        print("\n===== GROCERY SHOPPING LIST =====")
        print("1. Add item")
        print("2. View list")
        print("3. Remove item")
        print("4. Search item")
        print("5. Sort list")
        print("6. Clear list")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            search_item()
        elif choice == "5":
            sort_items()
        elif choice == "6":
            clear_list()
        elif choice == "7":
            print("Thank you for using the Shopping List App.")
            break
        else:
            print("Invalid choice. Please choose 1 to 7.")


main()
