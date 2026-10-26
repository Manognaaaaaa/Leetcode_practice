
'''
Time Complexity --> o(n)
Space Complexity --> o(n)

'''
def two_sum(lst, target):
    seen = {}
    for i, x in enumerate(lst):
        if target - x in seen:
            return i, seen[target - x]
        seen[x] = i
    return None


nums = [4,5,6]
target = 10
print(two_sum(nums, target))