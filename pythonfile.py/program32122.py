#def count_digit(n):
n = 213
digits = []
while n > 0:
     x = n % 10
     digits.append(x)     
     n //= 10
     print(x, end="")
for d in reversed(digits):
     
      print(d, end="")     
   