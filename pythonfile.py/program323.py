def Num_count(a, b):
    for i in range(a, b+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)

a = int(input("Enter starting number : ")) 
b = int(input("Enter ending number : ")) 

Num_count(a, b)            