import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

mask = np.array([False, True, False, True, False, True, False, True, False, True])

masked_array = np.ma.masked_array(data, mask=mask)

print("Original Array:")
print(data)

print("\nMasked Array:")
print(masked_array)