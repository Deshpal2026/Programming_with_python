class Student:#creating a calss
    def __init__(self, name):  #constructor method to initialize the object
        self.name = name     #instance variable to store the name

    def study(self):        #method to print the name of the student who is studying
        print(self.name, "is studying")#creating an object of the student class and passing the name argument to the constructor

s1 = Student("Amit")#creating an object of the student class and passing the name argument to the constructor
s1.study()#calling the study method of the S1 object to print the name of the student who is studying 
s2 = Student("Priya")           #creating another object of the student class and passing the name argument to the constructor