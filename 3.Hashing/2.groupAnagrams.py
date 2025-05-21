from collections import defaultdict
def anagram(strs):
    strs_dict = defaultdict(list) # creatting default list
    result = []
    for s in strs:
        sorted_s = tuple(sorted(s))
        strs_dict[sorted_s].append(s)
    for value in strs_dict.values():
        result.append(value)
    return result 

print(anagram(["eat","tea","tan","ate","nat","bat"]))

 