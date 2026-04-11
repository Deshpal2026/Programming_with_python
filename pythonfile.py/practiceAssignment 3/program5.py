# Create empty dictionary
students = {}

while True:
    print("\nMENU")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    # A - Add student
    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    # B - Update marks
    elif choice == 'B':
        name = input("Enter student name: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated!")
        else:
            print("Student not found!")

    # C - Search student
    elif choice == 'C':
        name = input("Enter student name: ")
        if name in students:
            print(name, "marks:", students[name])
        else:
            print("Student not found!")

    # D - Display all
    elif choice == 'D':
        if students:
            print("\nAll Students:")
            for name, marks in students.items():
                print(name, ":", marks)
        else:
            print("No data available")

    # Exit
    elif choice == 'E':
        print("Program ended")
        break

    else:
        print("Invalid choice! Try again.")