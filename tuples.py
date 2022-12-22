"""
They are just arrays that can't be changed, so we can only index them
"""
tup = (1, 2, 3) # Create them with parentheses

print(tup)
print(tup[0])
print(tup[-1])


"""
Tuples are mainly used for keys for hashmaps or hashsets, because lists cannot
be keys. Lists are not hashable so we use tuples instead
"""
hashmap = { (1, 2, 3):6, (4, 5, 6):15 } # We are using the tuples as keys
print(hashmap)

newset = set() # Think of it like an array
newset.add((1, 2))

print(newset)
print((1, 2) in newset)