def count_digits(n):
    count = 0

    while n > 0:
        n = n // 10   # remove last digit
        print(n)
        count += 1    # increase count

    return count

# Example
n = int(input("Enter number :"))
print(count_digits(n))   # Output: 3
