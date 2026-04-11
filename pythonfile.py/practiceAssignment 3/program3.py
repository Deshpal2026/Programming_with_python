#take two list from user,  mearge them into one list and sort the result
list1 = list(map(int,input("Enter a number seperated by single space : ").split()))
list2 = list(map(int, input("Enter number in secod list seperated by space :").split()))
list3 = list1 + list2
print(list3)
list3 = sorted(list3)
print(list3)