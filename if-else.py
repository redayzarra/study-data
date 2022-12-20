"""
If statments don't need parentheses
"""
n = 1
if n > 2:
  n -= 1

elif n == 2:
  n += 2

else:
  pass


"""
Parentheses needed for multi-line conditions
"""
n, m = 1, 3
if ((n > 2 and
     n != m) or n == m):
     n += 1