"""
Classes are like blueprints, or species. Instance objects are like individuals
of the species. For example, you can have a class called Robot (with tons of
properties and functions)... then you can assign a variable and create a intance
object that is a robot with all those properties and functions filled out.
"""
class MyClass:

  def __init__(self, nums): #This is our constructor, self is passed into every method of a class. It's basically means "this"
    self.nums = nums # Creating a member variable nums and assigning it to the nums value passed in the parameter
    self.size = len(nums) # So this is a member variable called size that is assigned to the length of nums
  
  def getLength(self): #We can create methods, or member functions, this way - we must always pass in the self parameter so we can have access to our member variables
    return self.size

  """
  To call a member function inside another member function, we must always use
  the self parameter and use self to call it
  """
  def getDoubleLength(self): 
    return 2 * self.getLength() #Gets the value of getLength()