#WAP to print the first N natural numbers using recursion
#umber = int(input("Enter a number to find the sum of first N natural numbers: "))
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1) #recursive call to the function itself with n-1 until it reaches the base case
number = int(input("Enter a number to find the sum of first N natural numbers: "))
print(sum(number)) #function call