import heapq

#Sorting
#time --> o(nlogn) remember sorting is always o(nlogn) 
#space --> o(n)
def k_frequent(nums,k):
    count={}
    for num in nums: #o(n)
        count[num]=1+count.get(num,0)
    
    arr=[] 
    for num,cnt in count.items(): #o(m)
        arr.append([cnt,num])
    arr.sort() #o(mlogm)

    res = []
    while len(res)<k: #o(k)
        res.append(arr.pop()[1])
    return res 


#Min heap 
# n --> length of array 
# k --> number of top frequent elements
# time --> o(nlogk) --> log k because of type of heap sorting
# space --> o(n+k)
'''
1. Build a frequency map using dictionary 
2. build a min heap os size k 
    - here list acts as a heap
    - push the frequency first and then the num
    - pop the heap with the least freq
3. append the num values(heap[1]) into a result list'''
def k_frequent(nums,k):
    count={}
    for num in nums:
        count[num]=1+count.get(num,0)

    heap=[]
    for num in count.keys():
        heapq.heappush(heap,(count[num],num))
        if len(heap)>k:
            heapq.heappop(heap)

    res=[]
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res 


# Bucket sort --> BEST METHOD
# Time --> o(n)
# Space --> o(n)
'''
1. create freq list which is the size of nums
2. create the freq map in count dictionary
3. enter the values into freq 
    - consider the values as the index 
    - enter the key into the list at the respective index
    - can be a list inside a list 
4. appened k items into the res list
    - go from back of the list to front'''
def k_frequency(nums,k):
    count={}
    freq=[[] for _ in range(len(nums) + 1)]

    for num in num:
        count[num] = 1+count.get(num,0)
    for num,cnt in count.items():
        freq[cnt].append(num)
    
    res = []
    for i in range(len(freq)-1,0,-1):
        for num in freq[i]:
            res.append(num)
            if len(res)==k:
                return res