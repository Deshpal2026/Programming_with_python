def print_digits(n):
     digits = []

     while n > 0:
        digit = n % 10
        digits.append(digit)
        #n = n //10

     for d in reversed(digits):
        print(d , end="")

print_digits(321)  


