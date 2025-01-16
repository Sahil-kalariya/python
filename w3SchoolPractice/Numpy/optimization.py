import numpy as np
large_array = np.random.rand(1_000_000)

def sum_using_loop(array):
    total = 0.0
    for element in array:
        total += element
    return total

sum_loop = sum_using_loop(large_array)
print("Sum using for loop:", sum_loop)

sum_numpy = np.sum(large_array)
print("Sum using NumPy's built-in function:", sum_numpy)
