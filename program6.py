principal = str(input("Enter the principal amount: "))
rate = str(input("Enter the rate of interest: "))
time = str( input("Enter the time in years: "))
simple_interest = (float(principal) * float(rate) * float(time)) / 100
print("The simple interest is " + str(simple_interest))
