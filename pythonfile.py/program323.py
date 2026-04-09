def Num_count(a, b):
    for i in range(a, b+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)
    
Num_count(1, 100)            