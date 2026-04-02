def digit_Number(n):
     digit = []
     count = 0
     for i in str(n) :
         count += int(i)
         digit.append(int(i))
     print(count)
     print(digit)
     return 0
    
n = int(input("Enter a number : "))
digit_Number(n)

        