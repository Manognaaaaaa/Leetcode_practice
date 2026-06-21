#Brute Force Solution - O(n^2)
nums = [4,5,6]
target = 10
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i, j])


#hashmap solution - O(n)
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # no solution (won't happen per constraints)

print(two_sum([4,5,6], 10))   # [0, 2]
print(two_sum([3,4,5,6], 7))  # [0, 1]
print(two_sum([5,5], 10))     # [0, 1]

