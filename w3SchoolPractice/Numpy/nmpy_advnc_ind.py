import numpy as np

array_2d = np.random.randint(0, 100, size=(5, 5))

mask = array_2d > 50

selected_elements = array_2d[mask]

print('Original 2D array:\n', array_2d)
print('Mask array (elements > 50):\n', mask)
print('Selected elements using the mask:\n', selected_elements)