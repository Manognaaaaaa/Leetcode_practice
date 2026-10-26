'''
Time compelxity --> o(n)
Space Complexity --> o(n)
'''

def cd(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

nums = [1, 2, 2, 4]
print(cd(nums))