import itertools as it
def test(lst):
    result = [ list(x[1]) for x in it.groupby(lst, lambda x: x == 0) if not x[0] ]
    return result
nums = [3,4,6,2,0,0,0,0,0,0,6,7,6,9,10,0,0,0,0,0,7,4,4,0,0,0,0,0,0,5,3,2,9,7,1]
print("\nOriginal list:")
print(nums)
print("\nExtract non_zero block from a given integers of list:")
print(test(nums))