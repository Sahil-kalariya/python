import numpy as np

dtype = [('name', 'U10'), ('age', 'i4'), ('height', 'f4')]

structured_array = np.array([
    ('Lehi Piero', 25, 5.5),
    ('Albin Achan', 30, 5.8),
    ('Zerach Hava', 35, 6.1),
    ('Edmund Tereza', 40, 5.9),
    ('Laura Felinus', 28, 5.7)
], dtype=dtype)

print("Structured Array:")
print(structured_array)