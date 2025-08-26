import math

def mean(nums):
    return sum(nums)/len(nums)  # missing space around /

def median(nums):
    nums.sort()
    n = len(nums)
    mid = n // 2
    if n %2 ==0:   # missing spaces
        return (nums[mid-1]+nums[mid])/2
    return nums[mid]

def std_dev(nums):
    m = mean(nums)
    return math.sqrt(sum((x-m)**2 for x in nums)/len(nums))

numbers = [2,5,7,3,8,10]
print("Mean:", mean(numbers)
print("Median:", median(numbers)) #intentional mistake to test pylint
print("Standard Deviation:", std_dev(numbers)
