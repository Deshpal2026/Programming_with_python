class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
class CollegeManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        student = Student(name, roll)
        self.students[roll] = student
        print("Student Added Successfully!")

    def view_students(self):
        if not self.students:
            print("No students found")
        else:
            for roll, student in self.students.items():
                print(f"Roll: {student.roll}, Name: {student.name}")
