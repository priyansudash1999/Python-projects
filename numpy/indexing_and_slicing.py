import numpy as np

# indexing - 
"""
numpy use zero base indexing
-ve indexing also 

syntax:- 
  array[index] -- for 1d array
  array[row, col] --  for multidimenstional array
"""

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])


# slicing :-

"""
extracting subarray from array

syntax :- 
  arr[start: end]  end is excluded like range function in python
"""

array = np.array([10, 20, 30, 40, 50, 60, 70])
print(array[1: 5]) # 2nd index to 4th index
print(array[:2]) # 0th to 1st index
print(array[::2]) # every second element
print(array[::-1]) # reverse


# Fancy indexing :- 
"""
Selecting multiple elements at once
syntax :- array[[what to select]]

"""

print(array[[0, 2, 4]])

# Boolean masking

"""
filter element according to condition

Syntax :- array [condition]
"""

print(array[array > 25])