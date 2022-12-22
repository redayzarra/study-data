"""
Hashsets allow us to search and insert values in constant time, O(1)
"""
hashset = set() # Initialize the set

hashset.add(1) #Add to the set, there cannot be any duplicates in hashsets
hashset.add(2)
print(hashset)

print(len(hashset)) # Gives us the length of the hashset


"""
We can easily check if a value is in a hashset by..
"""
print(1 in hashset)
print(2 in hashset)
print(34 in hashset)


"""
We can also remove values in constant time, O(1)
"""
hashset.remove(1)
print(hashset)


"""
We can create a hashset out of arrays by..
"""
array = [1, 2, 34, 1, 1, 4324, 234, 2, 1, 3]
print(set(array)) # Gets rid of all duplicate values


"""
We can also create hashsets with set comprehension
"""
newset = {i for i in range(5)} # Creates a hashset from numbers 0 to 4
print(newset)