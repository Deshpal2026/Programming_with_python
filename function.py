a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def cal_leter( a , b ):
    sum = a + b
    return sum
def cal_multiply( a , b ):
    product = a * b
    return product
def cal_divide( a , b ):
    if b != 0:
        quotient = a / b
        return quotient
    else:
        return "Error: Division by zero"
def cal_subtract( a , b ):
    difference = a - b
    return difference
print("Sum:", cal_leter(a, b))
print("Product:", cal_multiply(a, b))
print("Quotient:", cal_divide(a, b))
print("Difference:", cal_subtract(a, b))
num = int(input("Enter a number to find its factorial : "))
factorial = 1
for i in range(1 , num + 1):
    factorial *= i
print(factorial)







