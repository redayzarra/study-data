"""
O(1) - Constant time, meaning that the input size will not affect the time
it takes for the algorithm to run.
"""
#Arrays
numbers = [1, 2, 3, 4]
numbers.append(4) # Adding to the end of the array
numbers.pop() # Removing from the end of the array
numbers[0] # Looking up numbers at a given index

#Hashmaps / Hashsets
hashmap = {}
hashmap["key"] = 10 # Adding to the hashmap
"key" in hashmap # Returning the value from hashmaps
hashmap["key"] # Returning values from hashmaps
hashmap.pop("key") # Removing keys in hashmaps


"""
O(n) - Linear time, meaning that size of the input is directly proportional to
the time it takes for the algorithm to run.
"""
#Arrays
nums = [2, 3, 5]
sum(nums) # Sums of array 
for x in nums: # Looping through the array
  print(x)

nums.insert(1, 100) # Inserting elements in the middle of the array (adding int 100 at index 1)
nums.remove(3) # Removing elements in the middle of the array (removing int 3)
print(100 in nums) # Searching for an element

import heapq
heapq.heapify(nums) # Building a heap 


"""
O(n^2) - Exponential time, meaning that you are most likely iterating through 
the input's sub-input as well which increases time exponentially
"""
nums2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(nums2)): # Traversing through a square grid
    for j in range(len(nums2[i])): 
        print(nums2[i][j])

nums3 = [1, 2, 3]
for i in range(len(nums3)): # Get every pair of elements in array
    for j in range(i + 1, len(nums3)):
        print(nums3[i], nums3[j])

# Insertion sort (insert in middle n times -> n^2)