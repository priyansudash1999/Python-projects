import numpy as np

arr = np.array([10, 20, 22, 40, 50, 60])

new_arr = arr.reshape(2, 3)
print(new_arr)



arr_ravel = new_arr.ravel()
arr_flat = new_arr.flatten()
print(arr_ravel)
print(arr_flat)

# manipulating array

#  insert

arr_ = np.array([1,2,3])

new_arr_ = np.insert(arr_, 2, 100, axis=0) # axis is for row and col

print(arr_)
print(new_arr_)


# insert element in 2d arr
arr_2d = np.array([[1,2], [3, 4]])
new_2d_arr = np.insert(arr_2d, 1, [10, 1], axis=0)
print(new_2d_arr)

# append

app_append = np.append(arr_2d, [10, 20])
print(app_append)

# concat

arrrr = np.array([1, 2, 3])
arrry = np.array([5, 6, 7])
new_arraaay = np.concatenate((arrrr, arrry))
print(new_arraaay)

# delete
arrrrrrrr = np.array([7,8,9,10])
arrayaya = np.delete(arrrrrrrr, 0)
print(arrayaya)

arria_2d = np.array([[1, 2], [3, 4]])
new_arrria_2d = np.delete(arria_2d, 0, axis=0)
print(new_arrria_2d)