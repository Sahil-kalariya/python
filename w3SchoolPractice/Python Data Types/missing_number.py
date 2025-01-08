import array as arr
def test(nums):
    return sum(range(10, 21)) - sum(list(nums))

nums = [10, 11, 12, 13, 14, 16, 17, 18, 19, 20]

print(test(nums))