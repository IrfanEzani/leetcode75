#!/usr/bin/env python3

from collections import defaultdict

def twoSum(nums: list[int], target: int) -> list[int]:
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        # complement number for target
        # i.e. if target = 8, num = 3, complement = 5
        complement = target - num
        # if complement is in the dict, return the index
        if complement in dic:
            return [dic[complement], i]
        
        # add curr elem as key, and the index as val
        dic[num] = i 
    
    return [-1, -1]

def repeatedCharacter(s: str) -> str:
    chars = set()
    for i in s:
        if i in chars:
            return i
        else:
            chars.add(i)
    return ""

def findNumbers(nums: list[int]):
    ans = []
    num_set = set(nums)
    
    for num in num_set:
        if (num + 1 not in num_set) and (num - 1 not in num_set):
            ans.append(num)
    return ans
def checkIfPangram(sentence: str) -> bool:
    # set of all alphabets
    char_set = set("thequickbrownfoxjumpsoverthelazydog")
    sentence_set = set(sentence)
    # check 
    for char in char_set:
        if char not in sentence_set:
            return False
    return True

def missingNumber(nums : list[int]) -> int:
    #res = set([i for i in range(len(nums)+1)])
    num_set = set(nums)
    n = len(nums) + 1
    for i in range(n):
        if i not in num_set:
            return i

def countElements(arr: list[int]) -> int:
    ans = 0
    res = set(arr)
    for i in arr:
        if i+1 in res:
            ans += 1  
    return ans  

'''
Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.
'''
def intersection(nums: list[list[int]]) -> list[int]:
    counts = {}
    n = len(nums)
    
    # fill hash maps by iterating through the list
    for arr in nums:
        for i in arr:
            counts[i] = counts.get(i, 0) + 1
    
    res = []
    
    # iterate through keys
    #for i in counts:
    #    # if val == n, add to res arr.
    #    if counts[i] == n:
    #        res.append(i)
    
    return sorted([key for key,val in counts.items() if val == n])    

def areOccurrencesEqual(s: str) -> bool:
    count = {}
    for i in s:
        count[i] = count.get(i, 0) + 1
    
    res = set([v for _, v in count.items()])
    
    return (len(res) == 1)

def subarraySum(nums: list[int], k: int) -> int:
        counts = {0:1}
        ans = curr = 0

        for num in nums:
            # curr = prefix count
            curr += num
            # if curr - k exists in the hash table
            if curr - k in counts:
                # add value to counter
                ans += counts[curr - k]
            
            # update hash table with new key (which is curr) and value
            counts[curr] = counts.get(curr, 0) + 1
            
        
        return ans

def oddSubarray(nums: list[int], k: int) -> int:
    curr = ans = 0
    counts = {0:1}
    
    for n in nums:
        curr += n % 2
        if curr - k in counts:
            ans += counts[curr-k]
        
        counts[curr] = counts.get(curr, 0) + 1
    
    return ans
    
    
def main():
    print(oddSubarray([1, 1, 2, 1, 1], 3))
    
    #print(areOccurrencesEqual("aaabb"))
    #nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
    #print(intersection(nums))
    #print(countElements([1,1,2,2]))
    #print(twoSum([5,2,7,10,3,9], 8))
    #print(checkIfPangram("abcdeda"))
    #missingNumber([9,6,4,2,3,5,7,0,1])
    return 0

if __name__ == "__main__":
    main()