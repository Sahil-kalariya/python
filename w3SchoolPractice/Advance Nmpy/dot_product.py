import numpy as np
nums1 = np.array([[1, 2], [3, 4], [5, 6]])
nums2 = np.array([7, 8])
print("Original arrays:")
print(nums1)
print(nums2)
result = np.dot(nums1, nums2)
print("Dot product of the said two arrays:")
print(result)