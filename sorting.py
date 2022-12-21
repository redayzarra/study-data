"""
There are several ways to sort
"""
arr = [23, 35, 23, 2, 34, 1, 3]
arr2 = [343, 42, 34, 23, 234, 24, 4]
arr.sort() # Sorts the original array
print(arr)

sortedarr = sorted(arr2) # Creates a sorted copy of the original array
print(sortedarr)

"""
To sort in descending order...
"""
arr.sort(reverse=True) # Reverses the sorting order so descending order


"""
To custom sort, for example a length of a string...
"""
str = ["eye", "ashley", "faldjf", "idontknow", "a", "ae"]
str.sort(key = lambda x: len(x)) # The key that will be used for sorting will be the lambda function (which is a function without a name).. it will take every element (x) and return the length of x and use that as a key to sort
print(str)