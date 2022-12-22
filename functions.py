"""
Functions can be named anything, some take in parameters that can do fun things
or you can just leave it empty
"""

def function_name(x, y):
  return x * y

print(function_name(4, 5)) # We are calling the function with given arguments


"""
Nested functions are functions inside functions that can be used for recursive
problems because the inner functions can reference the outer functions
"""
def outer(a, b): # The outer function takes in parameters a and b
  c = "Carrot" # Declares the variale c

  def inner(): # Inner function is initialized
    return a + b + c # Inner function has access to c
  return inner() # The return value for the outer function is the value of inner

print(outer("a", "b")) # Print the output of outer with the given arguments


"""
In nested functions, you can modify objects but you can't reassign variables
for all functions unless you use the keyword nonlocal
"""
def double(arr, val):
  
  def helper():
    for i, n in enumerate(arr): # Iterate with the index value of current element
      arr[i] *= 2 # Modify the array by doubling the value at the index, this DOES update the original array

# But if we double val in the helper function, it will only do that in the 
# helper() function and not in the double() so we have to declare it nonlocal
    nonlocal val
    val *= 2

  helper() # Call the helper function with no arguments, as part of the double()
  print(arr, val)

nums = [x for x in range(1, 11)] # Gives us an array with 1 to 10
value = 10
double(nums, value)