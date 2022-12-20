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
the input's sub-input as well which increases time exponentially. Square grid.
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


"""
O(n*m) - Exponential time, but more referring to a rectangular array of size
n and width m. The time it would take would still look exponentail.
"""
nums4, nums5 = [1, 2, 3], [4, 5]
for i in range(len(nums4)): # Get every pair of elements from two arrays
    for j in range(len(nums5)):
        print(nums4[i], nums5[j])

nums = [[1, 2, 3], [4, 5, 6]]
for i in range(len(nums)): # Traverse rectangle grid
    for j in range(len(nums[i])):
        print(nums[i][j])


"""
O(n^3) - Exponential time, usually nested loop that iterate through an array
multiple times for every input
"""
nums6 = [1, 2, 3]
for i in range(len(nums6)): # Get every triplet of elements in array
    for j in range(i + 1, len(nums6)):
        for k in range(j + 1, len(nums6)):
            print(nums6[i], nums6[j], nums6[k])