class Cat:
    def sound(self): #method to print the sound of the cat
        print("Meow")

class Dog:
    def sound(self):#method to print the sound of the dog
        print("Bark")

for animal in (Cat(), Dog()):
    animal.sound()
