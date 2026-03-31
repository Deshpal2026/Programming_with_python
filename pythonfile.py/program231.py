# word = "artificial"
# count =0
# for ch in word :
#     if (ch == 'a' or 
#       ch == 'i' or 
#       ch == 'o' or 
#       ch == 'u' ):
#      count +=1
# print(count)        
# n =int(input("Enter n number "))
# sum = int((n*(n+1))/2)
# print(sum)
#print sum of first 'n' natural number.
n = int(input("Enter n natural number "))
sum = 0
for i in range(1, n+1 ):
    sum += i
print(sum)  
