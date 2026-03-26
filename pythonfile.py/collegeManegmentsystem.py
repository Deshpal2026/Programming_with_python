students = {}

# Add student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    students[roll] = name
    print("Student Added Successfully!")

# View students
def view_students():

    if not students:
        print("No students found")
    else:
        for roll, name in students.items():
            
            print(f"Roll: {roll}, Name: {name}")

# Menu
while True: 

    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice")