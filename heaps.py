import heapq

"""
Heaps are a common data structure to find the min and max of a set of values
"""
minHeap = [] # They are very similar to arrays


"""
To add values to heaps, we simply use...
"""
heapq.heappush(minHeap, 6)
heapq.heappush(minHeap, 5)
heapq.heappush(minHeap, 4)
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 1)
print(minHeap) # Looks like a normal array


"""
The minimum value in a heap will always be at index 0
"""
print(minHeap[0]) #The minimum value in the heap


"""
To loop through a heap while it's not empty...
"""
while len(minHeap):
  print(heapq.heappop(minHeap)) # Pops the first element from a heap


"""
To create a max heap, we simply use a min heap and multiply every value by -1
when we use push and pop
"""
maxHeap = [] # Initialize the heap

heapq.heappush(maxHeap, -6) # Multiply our true values with -1 while pushing
heapq.heappush(maxHeap, -5)
heapq.heappush(maxHeap, -4)
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -1)
print(maxHeap[0] * -1) # Gives us the max

while len(maxHeap):
  print(heapq.heappop(maxHeap) * -1) # Muliply again by -1 for true value


"""
If you already have values with which you want to make a heap from, you can do
it in linear time by using heapify
"""
array = [23, 434, 33, 432, 34, 24, 230, 4] # Given set of values

heapq.heapify(array) # Builds a heap in linear time, original is converted

while array: # While the array is not empty
  print(heapq.heappop(array)) # Lists the values in the array in ascending order