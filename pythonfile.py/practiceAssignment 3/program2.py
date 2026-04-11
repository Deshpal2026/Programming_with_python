#find average of list number

list = list(map(float,input("Enter numbers separated by space: ").split()))
total = sum(list)
count = len(list)
average = total // count


print(average)