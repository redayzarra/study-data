"""
Hashmaps are dictionaries and you can simply start them by...
"""
hashmap = {} # It's a dictionary, meaning it has key-value pairs


"""
To add values to hashmaps, simply state the key and the corresponding value
"""
hashmap["key_name"] = "value"
hashmap["newkey"] = "anothervalue"
print(hashmap)

print(len(hashmap)) # Gives us the number of keys the hashmap has, like entries


"""
To modify the value of a certain key, just reassign it...
"""
hashmap["firstName"] = "ReDay" # Created an entry for my first name
print(hashmap)
hashmap["firstName"] = "Ashley" # Then just reassigned it to something else
print(hashmap)


"""
We can search or remove if a key exists in a hashmap in constant time, O(1)
"""
print("key_name" in hashmap) # Is the key with that name there?

hashmap.pop("firstName") # Removed the specified key and its corresponding value
print(hashmap)


"""
To initialize a hashmap we can use the following format...
"""
newmap = {"integer": 1, "array": [1, 34, 43, 5], "string": "hello"}
print(newmap)


"""
We can use dict comprehension to create hashmaps efficiently
"""
mymap = {i:2*i for i in range(3)} # Creates a key (i) and assigns the doubled amount as the value
print(mymap)


"""
There are many ways of looping throug a hashmap - for keys, values, or both
"""
example = {x:(str(x)*2) for x in range(11)}

for key in example: # Iterate through every key in the hashmap
  print(key, example[key]) # Give us the key and its value

for val in example.values(): # Iterate through every value in the hashmap
  print(int(val)/10)

for key, value in example.items(): # Unpack the hashmap and assign them to work with both
  print(int(value)*key)