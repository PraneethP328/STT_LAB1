"""Simple stats calculator using mean, median, and standard deviation."""

import math

def mean(nums):
    """Return the mean of a list of numbers."""
    return sum(nums) / len(nums)

def median(nums):
    """Return the median of a list of numbers."""
    nums.sort()
    n = len(nums)
    mid = n // 2
    if n % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2
    return nums[mid]

def std_dev(nums):
    """Return the standard deviation of a list of numbers."""
    m = mean(nums)
    return math.sqrt(sum((x - m) ** 2 for x in nums) / len(nums))

numbers = [2, 5, 7, 3, 8, 10]
print("Mean:", mean(numbers))
print("Median:", median(numbers))
print("Standard Deviation:", std_dev(numbers))

