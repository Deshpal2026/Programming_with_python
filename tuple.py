tuple = (1, 2, 3, 4, 5 , "apple", "banana")  
# This is a tuple containing five integer items.
# Tuples are similar to lists but are immutable, meaning their items cannot be changed after creation.
# The items in the tuple can be accessed by their index, starting from 0.
print(tuple)
print(type(tuple))
print(len(tuple))
print(tuple[0]) #Accessing the first item
print(tuple[3]) #Accessing the forth element
print(tuple[-1]) #Accessing the last item, using negative indexing
print(tuple[1:4]) #Accessing a slice of the tuple from index 1 to 3
# tuple[2] = 10 #This will raise an error because tuples are immutable
# tuple.append(6) #This will raise an error because tuples do not support item assignment
# tuple.remove(3) #This will raise an error because tuples do not support item removal
# tuple.sort() #This will raise an error because tuples do not support sorting
tuple2 = (6, 7, 8)
tuple3 = tuple + tuple2 #Concatenating two tuples to create a new tuple
print(tuple3)
print(tuple3.index("banana")) #Finding the index of the item "banana"
print(tuple3.count(3)) #Counting occurrences of 3 in the tuple
# tuple.clear() #This will raise an error because tuples do not support clearing items
print(tuple3)
# Tuples do not support methods that modify the tuple, such as append, remove, sort, or clear.




