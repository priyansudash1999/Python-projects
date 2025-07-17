import numpy as np

arr_2d = np.array([[1,2,3], [4, 5,6]])
print(arr_2d.shape)
print(arr_2d.size)
print(arr_2d.ndim)
print(arr_2d.dtype)


# converting data types
arr_float = arr_2d.astype(float)
print(arr_float)
print(arr_float.dtype)


# Operator
arr = np.array([10, 20, 30])
print(arr+5)



# Aggregation function
arrray = np.array([10, 20, 30, 40])
print(np.sum(arrray))
print(np.mean(arrray))
print(np.min(arrray))
print(np.max(arrray))
print(np.std(arrray))
print(np.var(arrray))