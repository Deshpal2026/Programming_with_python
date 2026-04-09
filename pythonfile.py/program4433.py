def Is_prime(n):
    while n > 0 :
        if n % 2 == 0:
            
            print("True" )
            break

        else:
             
             print("False" )
             break
n = int(input("Enter a number : "))
Is_prime(n)
#result = Is_prime(n)
#print(result)                