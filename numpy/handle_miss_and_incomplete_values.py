import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])
print(arr)
print(np.isnan(arr))

print(np.nan == np.nan)

# nan to num
# new_arr = np.nan_to_num(arr, nan=[100,101])
# print(new_arr)

# infinity number handle
array1 = np.array([1, 2, np.inf, 8])
print(np.isinf(array1))

cleaned_arr = np.nan_to_num(array1, posinf=12000, neginf=1000)
print(cleaned_arr)