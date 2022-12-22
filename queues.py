from collections import deque # Import the queue

queue = deque() #Initialize the instance object
queue.append(1) # Adding values to the left of the queue
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)

queue.popleft() # We can pop values in O(1) time with queues
print(queue)

queue.pop() # We can pop from the right side like normal in O(1)

queue.appendleft(100) # We can add values to the left in O(1)
queue.appendleft(34)
print(queue)