items = []

def add_item():
    item = input("Enter grocery item: ").strip()

    if item == "":
        print("Item cannot be empty.")
    elif item.lower() in [x.lower() for x in items]:
        print("Item is already in the list.")
    else:
        items.append(item)
        print("Item added.")

def show_items():
    if len(items) == 0:
        print("Shopping list is empty.")
        return

    print("\nShopping List:")

    for i in range(len(items)):
        print(i + 1, ".", items[i])

def remove_item():
    show_items()

    if len(items) == 0:
        return

    try:
        number = int(input("Enter item number to remove: "))
    except ValueError:
        print("Please enter a whole number.")
        return

    if number >= 1 and number <= len(items):
        items.pop(number - 1)
        print("Item removed.")
    else:
        print("Invalid number.")

def search_item():
    search = input("Enter item to search: ").lower()
    found = False

    for item in items:
        if search in item.lower():
            print("Found:", item)
            found = True

    if found == False:
        print("Item not found.")

def sort_items():
    items.sort()
    print("Shopping list sorted.")

def clear_list():
    answer = input("Do you want to clear the list? (yes/no): ").lower()

    if answer == "yes":
        items.clear()
        print("List cleared.")
    else:
        print("List was not cleared.")

def main():
    while True:
        print("\n--- GROCERY SHOPPING LIST ---")
        print("1. Add item")
        print("2. Show list")
        print("3. Remove item")
        print("4. Search item")
        print("5. Sort list")
        print("6. Clear list")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            show_items()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            search_item()
        elif choice == "5":
            sort_items()
        elif choice == "6":
            clear_list()
        elif choice == "7":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

main()