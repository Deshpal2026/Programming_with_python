def Count_digit(n):
    count = 0
    while n > 0:
        x = n % 10
        count += x
        n//=10
    return count
n = int(input("Enter numbers : "))
result = Count_digit(n)
print(result)    