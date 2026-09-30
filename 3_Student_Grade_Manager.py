names = []
marks = []

def add_student():
    name = input("Enter student name: ")

    try:
        mark = float(input("Enter mark: "))
    except ValueError:
        print("Please enter a number.")
        return

    if name == "":
        print("Name cannot be empty.")
    elif mark < 0 or mark > 100:
        print("Mark must be between 0 and 100.")
    else:
        names.append(name)
        marks.append(mark)
        print("Student added.")

def get_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "D"

def show_students():
    if len(names) == 0:
        print("No students found.")
        return

    for i in range(len(names)):
        grade = get_grade(marks[i])
        print(i + 1, names[i], "-", marks[i], "-", grade)

def search_student():
    search = input("Enter student name: ").lower()
    found = False

    for i in range(len(names)):
        if search in names[i].lower():
            print(names[i], "-", marks[i], "-", get_grade(marks[i]))
            found = True

    if found == False:
        print("Student not found.")

def class_summary():
    if len(marks) == 0:
        print("No marks available.")
        return

    total = 0
    highest = marks[0]
    lowest = marks[0]

    for mark in marks:
        total = total + mark

        if mark > highest:
            highest = mark

        if mark < lowest:
            lowest = mark

    average = total / len(marks)

    print("Average mark:", average)
    print("Highest mark:", highest)
    print("Lowest mark:", lowest)

def delete_student():
    show_students()

    if len(names) == 0:
        return

    try:
        number = int(input("Enter student number to delete: "))
    except ValueError:
        print("Please enter a whole number.")
        return

    if number >= 1 and number <= len(names):
        position = number - 1
        names.pop(position)
        marks.pop(position)
        print("Student deleted.")
    else:
        print("Invalid number.")

def main():
    while True:
        print("\n--- STUDENT GRADE MANAGER ---")
        print("1. Add student")
        print("2. Show students")
        print("3. Search student")
        print("4. Class summary")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_summary()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

main()