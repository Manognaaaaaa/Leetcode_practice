# brute force approach 
# Time complexity: O(n^2)
# Space complexity: O(1)
def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False    

# Sorting approach
# Time complexity: O(n log n)
# Space complexity: O(1)
def contains_duplicate(nums):
    nums.sort()
    for i in range(1,len(nums)-1):
        if nums[i] == nums[i-1]:
            return True
    return False

# Caution: This modifies the input
#nums.sort()
# Safer: Sort a copy if original order matters
#sorted_nums = sorted(nums)


# Hashmap approach
# Time complexity: O(n)
# Space complexity: O(n)
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen: 
            return True
        seen.add(num)
    return False

#Hash Set length approach
# Time complexity: O(n)
# Space complexity: O(n)
def has_duplicate(nums):
    seen = set(nums) #adds all elements only once and ignores the duplicates
    return len(seen) != len(nums)
