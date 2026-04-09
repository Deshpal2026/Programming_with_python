def Sum_num(n):
    count = 0
    while n > 0:
        x = n % 10 
        count += x
        n //=10
    print(count)
Sum_num(223)        