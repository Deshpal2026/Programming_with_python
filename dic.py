
info = {
    "Student name" : "Andrew Park",
    "Student Id " : "809839",
    "Course" : "Information Technology",
}
print(info)
print(list(info.items()))
print(type(info))
print("Student name: " + info["Student name"])
print("Student Id: " + info["Student Id "])
print("Course: " + info["Course"])
info["Student name"] = "John Doe"
info["Course"] = "Computer Science"
print("Updated Student name: " + info["Student name"])
print("Updated Course: " + info["Course"])
print("Total number of items in the dictionary: " + str(len(info)))



