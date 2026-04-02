def facto_rial(n):
   fact = 1
   for i in range(1, n + 1):
     fact *= i
   return fact  
     
n = int(input("Enter number n :"))
result = facto_rial(n)
print(result)  
