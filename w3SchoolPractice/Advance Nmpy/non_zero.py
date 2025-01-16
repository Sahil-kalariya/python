import numpy as np
arr = np.array([0, 0, 0, 1, 0])
any_nonzero = np.any(arr != 0)
print(any_nonzero)