def Even_Num(a,b):
    even_list = []

    for i in range(a, b +1):
          if i % 2 == 0:
              even_list.append(i)
              #print(even_list)
    return even_list
    #print(even_list) 

a  = int(input("Enter number a  "))
b = int(input("Enter number  b  "))
result = Even_Num(a,b)
print(result)

      


