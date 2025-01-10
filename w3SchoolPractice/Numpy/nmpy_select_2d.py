import numpy as np

array_2d = np.random.randint(0, 100, size=(5, 5))

threshold = 50
selected_elements = array_2d[array_2d > threshold]

print('Original 2D array:\n', array_2d)
print(f'\nElements greater than {threshold}:\n', selected_elements)