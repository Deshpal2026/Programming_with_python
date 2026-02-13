class Animal:
    def speak(self):             #method to print the sound of the animal
        print("Animal speaks")

class Dog(Animal):
    def bark(self):                  #method to print the sound of the dog
        print("Dog barks")

d = Dog()
d.speak()
d.bark()
