import numpy as np

python_list = [1, 2, 3]
print("Original Python list:",python_list)
print(type(python_list))
numpy_array = np.array([4, 5, 6])
print("\nOriginal NumPy list:",numpy_array)
print(type(numpy_array))
combined_list = python_list + numpy_array.tolist()
print("\nCombined list:")
print(combined_list)
print(type(combined_list))