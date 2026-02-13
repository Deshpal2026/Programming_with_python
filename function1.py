class Student: #creating a class

    def __init__(self, name, age):#constructor method to initialize the object

        self.name = name #instance variable to store the name
        self.age = age #instance variable to store age

s1 = Student("Rahul", 22)#reating an object of the student class and passing the name and age arguments to the constructor
print(s1.name)#accessing the name attribute of the S1 object and printing it 
print(s1.age)
s2 = Student("Anushka Shukla", 22)#another object of the student class and passing the name and age argument to the constructor
print(s2.name)
print(s2.age)