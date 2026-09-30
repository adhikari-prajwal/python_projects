

students = []


def add_student():
    print("\n--- Add Student ---")
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        mark = float(input("Enter mark (0-100): "))

        if mark < 0 or mark > 100:
            print("Mark must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    students.append({"name": name, "mark": mark})
    print("Student added successfully.")


def get_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "D"


def view_students():
    print("\n--- Student Records ---")

    if not students:
        print("No student records available.")
        return

    for number, student in enumerate(students, start=1):
        grade = get_grade(student["mark"])
        print(f"{number}. {student['name']} - "
              f"{student['mark']:.1f} - Grade {grade}")


def search_student():
    if not students:
        print("No student records available.")
        return

    name = input("Enter student name to search: ").strip().lower()
    found = False

    for student in students:
        if student["name"].lower() == name:
            print(f"Name: {student['name']}")
            print(f"Mark: {student['mark']:.1f}")
            print(f"Grade: {get_grade(student['mark'])}")
            found = True

    if not found:
        print("Student not found.")


def class_summary():
    if not students:
        print("No student records available.")
        return

    total = 0
    highest = students[0]
    lowest = students[0]

    for student in students:
        total += student["mark"]

        if student["mark"] > highest["mark"]:
            highest = student

        if student["mark"] < lowest["mark"]:
            lowest = student["mark"]

    average = total / len(students)

    print("\n--- Class Summary ---")
    print(f"Number of students: {len(students)}")
    print(f"Average mark: {average:.2f}")
    print(f"Highest: {highest['name']} ({highest['mark']:.1f})")
    print(f"Lowest: {lowest['name']} ({lowest['mark']:.1f})")


def delete_student():
    view_students()

    if not students:
        return

    try:
        number = int(input("Enter student number to delete: "))

        if number < 1 or number > len(students):
            print("Invalid student number.")
            return

        removed = students.pop(number - 1)
        print(f"{removed['name']} was removed.")

    except ValueError:
        print("Please enter a whole number.")


def main():
    while True:
        print("\n===== STUDENT GRADE MANAGER =====")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Class summary")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_summary()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please choose 1 to 6.")


main()
