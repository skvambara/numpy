import numpy as np
arr = np.array([[1,2,3],[2,3,4]] , dtype=np.float32)

print(repr(arr))

arr2 = np.array([2,3.4,"skh"])
print(repr(arr2))

c = arr
d = arr2.copy()
c[0][0] = 14
d[0] = 45
print(format(repr(arr)))

print(format(arr2))

# arr2 = arr2.astype(np.float16)

print(arr2.dtype)

arr3 = np.array([np.nan, 1, 2])
print(repr(arr3))

#np.array([np.nan, 1 , 2], dtype=np.int32)
np.array([np.nan, 1 , 2], dtype=np.float32)
#np.array([np.inf, 2], dtype=np.int32)
np.array([np.inf, 2], dtype=np.float32)

arr4 = np.array([np.nan, 2,3,4,5])
arr5 = arr4.copy()
arr5[0] = 10
print(repr(arr5))

print("Array with 5.1")

arr6 = np.arange(5.1)
print(repr(arr6))
#lower end inclusive, upper end exclusive, step size of 0.5 
arr7 = np.arange(0, 5.1, 0.5)
print(repr(arr7))

print("**linspace**")

arr8 = np.linspace(5,11,num=4)
print(repr(arr8))

