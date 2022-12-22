"""
Strings are very similar to arrays
"""
s = "abc"
print(s[0:2])


"""
Strings are not mutable, they can only be updated
"""
s += "def" # O(n) time complexity because it's creating a new string
print(s)


"""
Strings can also be converted into numbers for math
"""
print(int("234") + int("3434"))


"""
Numbers can also be converted into strings
"""
print(str(234) + str(3423)) # We're converting the numbers and then gluing them together


"""
To get the ASCII value of a character...
"""
print(ord("a")) # Gives us a way of identifying certain characters while still maintaining their order
print(ord("b"))


"""
To combine a list of strings, we can join them by...
"""
words = ["ab", "cd", "ef"]
print("".join(words)) # We are telling the function to join the strings in the array together with no space ("") in between