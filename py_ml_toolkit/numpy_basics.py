#Real-time usable numpy code snippets
import numpy as np
# Create a 1D array of integers from 0 to 9
#Parameters explained:
# np.arange(start, stop, step) - Creates an array with evenly spaced values within a given range.
# start: value is inclusive, and stop: value is exclusive.
# step: value determines the spacing between the values.
array_1d = np.arange(10)
print("1D Array:", array_1d)
# Create a 2D array (matrix) of shape (3, 4) filled with zeros
print("2D Array:")
array_2d = np.zeros((3, 4))
#Parameters explained:
# np.zeros(shape) - Creates an array filled with zeros.
# shape: parameter specifies the dimensions of the array.
print(array_2d)
# Create a 3D array (tensor) of shape (2, 3, 4) filled with ones
#Parameters explained:
# np.ones(shape) - Creates an array filled with ones.
# shape: parameter specifies the dimensions of the array.
array_3d = np.ones((2, 3, 4))
print("3D Array:")
print(array_3d)
#Other useful numpy operations
# Create an array of evenly spaced values between 0 and 1 with 10 elements
#Parameters explained:
# np.linspace(start, stop, num) - Creates an array of evenly spaced values over a specified range.
# start: value is inclusive, stop: value is inclusive, num: number of elements to generate.
array_even = np.linspace(0, 1, 10)
#output: [0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556 0.66666667 0.77777778 0.88888889 1.        ]
print("Evenly spaced array:", array_even)
# Create a random 2D array of shape (3, 3)
#Parameters explained:
# np.random.rand(d0, d1, ..., dn) - Creates an array of the given shape filled with random values
# from a uniform distribution over [0.0, 1.0).
# d0, d1, ..., dn: dimensions of the array.
array_random = np.random.rand(3, 3)
print("Random 2D Array:")
print(array_random)
# Create a random integer array of shape (2, 3) with values between 0 and 10
##Parameters explained:
# np.random.randint(low, high, size) - Creates an array of random integers from low (inclusive) to high (exclusive).
# low: lower bound (inclusive), high: upper bound (exclusive), size: shape of the output array.
array_random_int = np.random.randint(0, 10, (2, 3))
print("Random Integer Array:")
print(array_random_int)
# Reshape a 1D array into a 2D array
#Parameters explained:
# np.reshape(array, new_shape) - Reshapes an array to a new shape without changing its data.
# new_shape: tuple specifying the new shape of the array. array: the input array to be reshaped.
array_reshaped = array_1d.reshape((2, 5))  # Reshape to 2 rows and 5 columns
print("Reshaped Array:")
print(array_reshaped)
# Perform element-wise operations
array_sum = array_1d + 5  # Add 5 to each element
print("Element-wise addition (adding 5):", array_sum)
# Element-wise multiplication
array_product = array_1d * 2  # Multiply each element by 2
print("Element-wise multiplication (multiplying by 2):", array_product)
# Calculate the mean of the 1D array
#Parameters explained:
# np.mean(array) - Calculates the mean (average) of the elements in the array.
# array: the input array for which the mean is calculated.
array_mean = np.mean(array_1d)
print("Mean of 1D Array:", array_mean)
# Calculate the standard deviation of the 1D array
array_std = np.std(array_1d)
print("Standard Deviation of 1D Array:", array_std)
# Calculate the sum of all elements in the 1D array
array_sum_all = np.sum(array_1d)
print("Sum of all elements in 1D Array:", array_sum_all)
# Calculate the maximum and minimum values in the 1D array
array_max = np.max(array_1d)
array_min = np.min(array_1d)
print("Maximum value in 1D Array:", array_max)
print("Minimum value in 1D Array:", array_min)
# Transpose a 2D array
a = np.array([[1, 2, 3], [4, 5, 6]])
a_transposed = a.T
print("Transposed Array:", a_transposed)
# Concatenate two arrays along a specified axis
#Parameters explained:
# np.concatenate((array1, array2), axis) - Concatenates two or more arrays along a specified axis.
# array1, array2: input arrays to be concatenated, axis: axis along which the arrays are concatenated.
b = np.array([[7, 8, 9], [10, 11, 12]])
concatenated = np.concatenate((a, b), axis=0)  # Concatenate along rows
print("Concatenated Array:", concatenated)
# Stack two arrays along a new axis
#Parameters explained:
# np.stack((array1, array2), axis) - Stacks two or more arrays along a new axis.
# array1, array2: input arrays to be stacked, axis: axis along which the arrays are stacked.
stacked = np.stack((a, b), axis=0)  # Stack along a new axis
print("Stacked Array:", stacked)
# Stack two arrays along a new axis
# Create a mask to filter elements in the 1D array
print("Original Array:", array_1d)
mask = array_1d > 5  # Create a mask for elements greater than 5
filtered_array = array_1d[mask]  # Apply the mask to filter elements
print("Filtered Array (elements > 5):", filtered_array)
# most common numpy operations

# arange(): Return evenly spaced values within a given interval
# All the parameters explained of arange():
# start: Start of interval.
# stop: End of interval.
# step: Spacing between values. Default is 1.
arr = np.arange(0, 10, 2)

# linspace(): Return evenly spaced numbers over a specified interval
# All the parameters explained of linspace():
# start: The starting value of the sequence.
# stop: The end value of the sequence.
# num: Number of samples to generate. Default is 50.
# endpoint: If True (default), stop is the last sample.
# retstep: If True, return (samples, step)
arr = np.linspace(0, 1, num=5, endpoint=True, retstep=False)

# reshape(): Gives a new shape to an array without changing its data
# All the parameters explained of reshape():
# newshape: Tuple of ints, defining the new shape.
# order: 'C', 'F', 'A'. Read elements using C-style (row-major) or Fortran-style (column-major) order. Default is 'C'.
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape((2, 3))

# concatenate(): Join two or more arrays along an existing axis
# All the parameters explained of concatenate():
# arrays: Sequence of arrays to join.
# axis: Axis along which the arrays will be joined. Default is 0.
arr1 = np.array([[1, 2]])
arr2 = np.array([[3, 4]])
combined = np.concatenate((arr1, arr2), axis=0)

# where(): Return elements chosen from x or y depending on condition
# All the parameters explained of where():
# condition: Array-like, where True, yield x, otherwise yield y.
# x: Values from which to choose where condition is True.
# y: Values from which to choose where condition is False.
arr = np.array([10, 20, 30, 40])
result = np.where(arr > 25, 'High', 'Low')

# mean(): Compute the arithmetic mean along the specified axis
# All the parameters explained of mean():
# a: Array containing numbers whose mean is desired.
# axis: Axis along which the means are computed. Default is None (entire array).
# dtype: Type to use in computing the mean.
# keepdims: If True, retains reduced dimensions with length 1.
arr = np.array([[1, 2], [3, 4]])
mean_val = np.mean(arr, axis=0)

# std(): Compute the standard deviation along the specified axis
# All the parameters explained of std():
# a: Input array.
# axis: Axis along which standard deviation is computed. Default is None.
# ddof: Delta Degrees of Freedom. Default is 0.
# keepdims: If True, the reduced axes are left in the result as dimensions with size one.
arr = np.array([1, 2, 3, 4, 5])
std_val = np.std(arr)

# sum(): Sum of array elements over a given axis
# All the parameters explained of sum():
# a: Input array.
# axis: Axis or axes along which a sum is performed.
# dtype: The type of the returned array and of the accumulator.
# keepdims: If True, retains reduced dimensions with length 1.
arr = np.array([[1, 2], [3, 4]])
total = np.sum(arr, axis=1)

# argmax(): Return indices of the maximum values along an axis
# All the parameters explained of argmax():
# a: Input array.
# axis: Axis along which to find the maximum. Default is None (flattened array).
arr = np.array([[1, 7], [3, 4]])
idx = np.argmax(arr, axis=1)

# unique(): Find the unique elements of an array
# All the parameters explained of unique():
# ar: Input array.
# return_index: If True, also return the indices of the input array that give the unique values.
# return_inverse: If True, also return the indices to reconstruct the input array from the unique array.
# return_counts: If True, also return the number of times each unique item appears.
arr = np.array([1, 2, 2, 3, 1])
unique_vals, counts = np.unique(arr, return_counts=True)

# sort(): Return a sorted copy of an array
# All the parameters explained of sort():
# a: Array to be sorted.
# axis: Axis along which to sort. Default is -1.
# kind: Sorting algorithm (‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’). Default is 'quicksort'.
# order: When `a` is an array with fields, this argument specifies which fields to compare first.
arr = np.array([[1, 4], [3, 1]])
sorted_arr = np.sort(arr, axis=1)

# clip(): Limit the values in an array
# All the parameters explained of clip():
# a: Input array.
# a_min: Minimum value. All elements less than this will be set to this value.
# a_max: Maximum value. All elements more than this will be set to this value.
arr = np.array([1, 5, 10])
clipped = np.clip(arr, a_min=2, a_max=8)

# flatten(): Return a copy of the array collapsed into one dimension
# All the parameters explained of flatten():
# order: 'C' (row-major), 'F' (column-major), 'A' (fortran-style). Default is 'C'.
arr = np.array([[1, 2], [3, 4]])
flattened = arr.flatten(order='C')
