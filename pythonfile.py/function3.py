#encapsulation means hiding data so it is not changed directly.
class Bank:
    def __init__(self):                     #constuctor method to initialize the object
        self.__balance = 0                   #

    def deposit(self, amount):             #public method to modify the private variable
        self.__balance += amount           #modifying the private variable using a public method

    def show_balance(self):                #public method
        print("Balance:", self.__balance)  #accessing the private variable within the class

b = Bank()
b.deposit(1000)
b.show_balance()