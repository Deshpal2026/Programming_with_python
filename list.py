List = ["apple", "banana", "charry", "date", "elderberry", 2, 3.2]
# This is a list containing various items including strings and numbers.
# The list contains fruits and some numeric values.
# The items in the list can be accessed by their index, starting from 0.
# For example, List[0] woill return "apple"
print(List)
print(type(List))
print(len(List))
print(List[0]) #Accessing the first item
print(List[3]) #Accessing the forth element
print(List[-1]) #Accessing the last item, using negative indexing
print(List[1:4]) #Accessing a slice of the list from index 1 to 3
List.append("fig") #Adding an item to the end of the list
print(List)
List.remove(2) #Removing the item with value 2 from the list
print(List)
List[2] = "cherry" #Correcting the spelling of "cherry"
print(List)
#List.sort() #Sorting the list 
#print(List)
List2 = ["grape", "honeydew"]
List.extend(List2) #Extending the list by adding elements from another list
print(List)
List.reverse() #Reversing the order of the list
print(List)
#List.clear() #Clearing all items from the list
print(List)
List.insert(2, "blueberry") #Inserting an item at index 2
print(List)
print(List.index("banana")) #Finding the index of the item "banana"
print(List.count("cherry")) #Counting occurrences of "cherry" in the list
List.pop() #Removing and returning the last item of the list
print(List)
List.remove("date") #Removing the item "date" from the list
print(List)
List.append("oooo") #Adding 3.2 back to the list
print(List)


