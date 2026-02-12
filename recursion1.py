#find the factorial of a number using recursion 
number = int(input("Enter a number to find its factorial: "))
def fact(n):
    if(n ==0 or n == 1):#base case or stopping cindition 
    
        return 1 #factorial of 0 and 1 is 1.
    return n * fact(n-1) #recursive call to the function itself with n-1 until it reaches the base case 
print(fact(number)) #function call 

        