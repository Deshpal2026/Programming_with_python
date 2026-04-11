# Input tuple from user
t = tuple(map(int, input("Enter numbers (space separated): ").split()))

# Create even and odd tuples
even_tuple = tuple(x for x in t if x % 2 == 0)
odd_tuple = tuple(x for x in t if x % 2 != 0)

# Output
print("Even numbers tuple:", even_tuple)
print("Odd numbers tuple:", odd_tuple)