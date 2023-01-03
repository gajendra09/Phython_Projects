import numpy as np
arr = np.array([1, 2, 3, 6, 9])
print(arr)

arr_mult_dim = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_mult_dim)

arr_dim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]])
print(arr_dim)
print(arr[1]+arr[2])
print("2nd element on 1st row", arr_mult_dim[0, 1])
print(arr_dim[0, 1, 2])
print(arr_dim[1, 1, 2])
arr_dimm = np.array([[[1, 2, 3], [4, 5, 6]], [[2, 4, 6], [3, 5, 7]], [[7, 8, 9], [3, 2, 1]]])
print(arr_dimm[1, 1, 2])
print(arr_dimm[1, 1])
print("last element from 2nd dim:", arr_mult_dim[1, -1])
print(arr[0:2])
print(arr_mult_dim[0, 1:2])


