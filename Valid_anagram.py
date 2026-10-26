#sorting
# time --> o(nlogn + mlogm) --> nlogn for sorting
#space --> o(1) or o(n+m) 
def valid_anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    return sorted(str1) == sorted(str2)
    
print(valid_anagram("racecar","carrace"))
print(valid_anagram("jar","jam"))
print(valid_anagram("jar","jared"))

#Hash tables 
# time --> o(n+m) --> generalized version (since n==m it can also be o(n))
#space --> o(1) --> atmost 26 characters
def valid_anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    s1={}
    s2={}
    for i in range(len(str1)):
        s1[str1[i]] = 1 + s1.get(str1[i],0)
        s2[str2[i]] = 1 + s2.get(str2[i],0)
    return s1==s2

#Hash table using array --> valid only if both are lowercase
# t --> o(n+m) (or as i like to thing o(n))
# s --> o(1) 
def valid_anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    count=[0]*26
    for i in range(len(str1)):
        count[ord(str1[i])-ord('a')]+=1
        count[ord(str2[i])-ord('a')]-=1
    for value in count:
        if value!=0:
            return False
    return True
'''If its mixed case just [0]*58 and -ord("A") --> 58 because between Z and a theres other things 
theres six wasted slots.
Alternative is to use if/else and check if its lower or upper. Then subtract A or a accordingly then add 26 to the lower values'''

