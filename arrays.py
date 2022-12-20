"""
Arrays, or lists, are an easy-to-use simple data structure
"""
arr = [1, 2, 3]
print(arr)


"""
They can also be used like stacks
"""
arr.append(4) # O(1)
arr.append(5)
print(arr)

arr.pop() # O(1)
print(arr)


"""
We can also insert into the middle
"""
arr.insert(1, 6) # We are inserting the value 6 at index 1 also O(n)
print(arr)


"""
To index at an array
"""
print(arr[0]) # Looking at the value at index 0, which is O(1)

arr[0] = 3 # Reassigning the value at index 0 with 3, which is also O(1)


"""
To initialize an array of a certain size
"""
n = 6
arr = [1] * 6
print(arr)


"""
Indexing with negative numbers
"""
arr = [0, 2, 354, 6]
print(arr[-1]) # Returns the last value of the array
print(arr[-2]) # Returns the second to last value of the array


"""
Slicing arrays can be easily done by specifying the indices
"""
arr = [1, 33, 354, 54, 45, 645, 3]
print(arr[1:4]) # Prints the values from index 1 to 3
print(arr[1:8]) # Prints the entire array because it's len 7 


"""
Unpacking the arrays
"""
a, b, c = [1, 2, 3] # Assigns the values to the different variables
print(a, b, c) # However, the number of variables must match the len of array


"""
Looping through arrays is also very easy with for and while loops
"""
nums = [1, 2, 3]
for i in range(len(nums)):
  print(nums[i]) # Indirectly look up the value at index i and print it

for x in nums:
  print(x) # Or just straight up print the value


"""
To get both the index and it's value while looping
"""
nums = [1, 2, 3, 4, 5]
for index, num in enumerate(nums):
  print(index, num)


"""
To iterate through multiple arrays at the same time, use unpacking and helpers
"""
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2): # Basically combines the two arrays 
  print(n1, n2)


"""
To reverse an array, you can use the reverse function
"""
nums = [1, 3, 5]
nums.reverse()
print(nums)