def count_digit(n):
    if n == 0:
        return 1
    
    count = 0
    while n > 0:
        n //= 10
        print(n)
        count += 1
    return count
print(count_digit(243))    
