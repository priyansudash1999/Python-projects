import numpy as np

# creating arrays using different types

# from python lists, list to array
arr1 = np.array([1,2,3])


# with default values
arr2 = np.zeros(shape=3)
print(arr2)

arr_one = np.ones((2, 5))
print(arr_one)

arr_full_fun = np.full((3, 1), 7)
print(arr_full_fun)

# sequences of numbers

arr_seq = np.arange(10)  # syntax = np.arange(start, stop, step)
arr_odd = np.arange(1, 10, 2)
print(arr_seq)
print(arr_odd)


# creating identity matrix
arr_identity = np.eye(3)
print(arr_identity)

# random number matrix
arr_rand = np.random.rand(2)
print(arr_rand)  # get two random points numbers between 0 to 1
