import numpy as np
# stacking

"""
vstack -- vertical stack
hstack -- horizontal stack 
"""
arr1 = np.array([1, 2, 3])
arr = np.array([1, 2, 3])

print(np.vstack((arr1, arr)))
print(np.hstack((arr1, arr)))


# splitting -  divide in subarrays

"""
np.split()
np.hsplit()
np.vslipt()
"""

array= np.array([10, 20, 30, 40, 50, 60])
split_arr = np.split(array, 3)
print(split_arr)

arraay = np.array([[1,2], [3,4], [4, 5]])
vsplit_arr = np.vsplit(arraay, 3)
print(vsplit_arr)

hsplit_arr = np.hsplit(arraay, 2)
print(hsplit_arr)