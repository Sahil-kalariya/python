import numpy as np

original_1d_array = np.arange(20)
print("Original 1D array:\n", original_1d_array)

reshaped_matrix = original_1d_array.reshape(4, 5)
print("\nReshaped (4, 5) matrix:\n", reshaped_matrix)

sub_matrix = reshaped_matrix[:2, :3]
print("\nSliced (2, 3) sub-matrix:\n", sub_matrix)

print("\nStrides of the sub-matrix:\n", sub_matrix.strides)