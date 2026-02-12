def print_list(list, index):
    if index == len(list):#base case or stopping condition when index is equal to the length of the list, it means we have printed all the elements in the list, so we can
        return #stop thr recursion and return to the previous call
    print(list[index])#print the current element at the index
    print_list(list, index + 1) #recursive call to the function itself with index + 1 until it reaches the base case where index is equal to the length of the list.
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print_list(names, 0)#function call with the list of names and starting indes 0 to prnt the first element in the list 
