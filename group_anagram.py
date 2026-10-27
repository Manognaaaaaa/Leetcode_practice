'''
Time complexity --> o(m*n)
Space complexity -->o(m) without output
                -->o(m*n) with output
'''

from collections import defaultdict
def ga(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c) - ord('a')] +=1
            res[tuple(count)].append(s)
        return list(res.values())

