"""
Python is decimal division by default
"""
print(5/2)


"""
To round down, we have to use //
"""
print(5//2)


"""
This means negative numbers will also round down!
"""
print(-3 // 2) # Rounds down to -2 instead of rounding towards zero

print(int(-3 // 2)) # The int helps round towards zero


"""
Modular operator gives us the remainder of a division
"""
print(10 % 3) # You can only get to 9 so only 1 will be left over

print(-10 % 3) # Prints 2? Weird stuff happens when you use mod with negatives...


"""
For consistency we use other language modulos
"""
import math
print(math.fmod(-10, 3)) # This will give us -1 instead of 2 <:

print(math.floor(3 / 2)) # Forcefully rounds down

print(math.ceil(3 / 2)) # Forcefully rounds up

print(math.sqrt(2)) # Takes the accurate square root

print(math.pow(2, 4)) # Gives us 2 to the power of 4


"""
For maximum integers and minimum integers
"""
float('inf')
float('-inf')