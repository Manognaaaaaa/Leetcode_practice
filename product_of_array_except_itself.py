#Brute force
#time --> o(n^2)
#space -->o(n)
def produ(nums):
    prod=[1]*len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j:
                prod[i]*=nums[j]
    return prod
# print(produ([-1,0,1,2,3]))

#Division
#time --> o(n)
#space --> o(1) extra space or o(n) for the output array 
'''
1. zero cnt and product
    - calculate product except 0
    - if its 0 increase the count
2. check if no of zero>1
    - if it is then the output array is 0 for every element
3. zero <= 1
    - the value is 0 for every element other than 0 and prod for 0 --> if theres a 0
    - no zer0 --> prod/nums[i]'''
def produ(nums):
    prod, zero_cnt = 1,0
    for num in nums:
        if num:
            prod*=num
        else:
            zero_cnt +=1
    if zero_cnt > 1: return [0]*len(nums)

    res = [0]*len(nums)
    for i,c in enumerate(nums):
        if zero_cnt: res[i]=0 if c else prod
        else: res[i] = prod//c
    return res


#Prefix and Suffix 
#time --> o(n)
#space --> o(n)
'''
1.create two array suffix and prefix
2. calculate suffix and prefic for each element
3. multiply suffix and prefix and thats ur ans
4. prefix of first element is 1 and suffix of last element is 1'''
def produ(nums):
    n = len(nums)
    res = [0]*n
    pref = [0]*n
    suf = [0]*n

    pref[0] = suf[n-1] = 1
    for i in range(1,n):
        pref[i] = nums[i-1]*pref[i-1]
    for i in range(n-2,-1,-1):
        suf[i]=nums[i+1]*suf[i+1]
    for i in range(n):
        res[i]=pref[i]*suf[i]
    return res


#Prefix and suffix(optimal)
#time --> o(n)
#Space --> o(1) and o(n) for result
'''First calculate the prefix and then multiply by postfix'''
def produ(nums):
    res = [1]*len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        res[i]*=postfix
        postfix *=nums[i]
    return res