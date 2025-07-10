#!/usr/bin/env python3

from collections import Counter, defaultdict

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
    
def findWinners(matches: list[list[int]]):
    winners = []
    losers = []
    dic = {}
    for match in matches:
        winner, loser = match
        dic[winner] = dic.get(winner, 0)
        dic[loser] = dic.get(loser, 0) + 1
        #print(f"winner: {winner}, loser: {loser}")
    
    for k, v in dic.items():
        if v == 0:
            winners.append(k)
        if v == 1:
            losers.append(k)
        
    return [sorted(winners), sorted(losers)]        
    
def largestUniqueNumber(nums:list[int]):
    dic = {}
    res = -1
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
   
    for k, v in dic.items():
        if v == 1:
            res = max(res, k)
    
    return res

def maxNumberOfBalloons(text: str) -> int:
    balloon_dict = Counter("balloon")
    text_dict = Counter(text)
    
    res = len(text)
    
    for i in balloon_dict:
        print(f"{i}: {text_dict[i]}|{balloon_dict[i]}")
        res = min(res, text_dict[i]//balloon_dict[i])
    
    return res   
    
def findMaxLength(nums: list[int]) -> int:
    
    '''
    hash map, maps values of count to the first index where that count was seen.
    maintain value of count and at each index
    KEY POINT: if we have seen the same value of count before: 
        subarray starting from where we saw that value of count, 
        and ending at the current index = equal number of 0s and 1s. 
    '''
    count = 0
    '''
    count: store the relative number of ones and zeros.
    + 1 when we see 1, -1 when we see 0.
    when count = 0, means we saw equal n of 1s and 0s.
    
    when we find the same count appears twice: 
    also means n of 1s and 0s are equal between the indices.
    '''
    res = 0
    dic = {0:-1} # for count: 0 at idx -1
    
    # added
    sub_arr_counts = 0
    '''
    tracking the indices corresponding to the same count value,
    we can get the max length of the subarray.
    '''
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
            
        # if count not in hash map, add to it
        if count not in dic:
            dic[count] = i
        else:
            print(f"subarray found at index {dic[count]} to {i}:")
            print([nums[i] for i in range(dic[count]+1, i+1)])
            sub_arr_counts += 1
            res = max(res, i - dic[count])
            
    
    
        
    return res
               
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    dic = defaultdict(list)
    for str in strs:
        keys = "".join(sorted(str)) # sorted version 
        dic[keys].append(str)
    
    return list(dic.values())

def minimumCardPickup(cards: list[int]) -> int:
    dic = defaultdict(list)
    for c in range(len(cards)):
        dic[cards[c]].append(c)
    
    res = 0
    for k in dic:
        arr = dic[k]
        for i in range(len(arr) - 1):
            #print(f"subarr len: {arr[i+1]} - {arr[i]}: {arr[i+1] - arr[i] + 1}")
            res = max(res, arr[i+1] - arr[i]+1)
    
    return res

# O(N) space complexity version
def minCardPickup(cards: list[int]) -> int:
    dic = {}
    min_len = float('inf')
    for i in range(len(cards)):
        if cards[i] in dic:
            min_len = min(min_len, i - dic[i] + 1)
        dic[cards[i]] = i
    
    return min_len if min_len != float('inf') else -1
    
# 2342
def maximumSum(nums: list[int]) -> int:
    def digitSum(n: int):
        sum = 0
        while n:
            sum += n % 10 
            n //= 10    
        return sum
    
    dic = {}
    ans = -1
    
    for num in nums:
        sum = digitSum(num)
        if sum in dic:
            ans = max(ans, num + dic[sum])
        dic[sum] = max(dic.get(sum, 0), num)
    
    return ans

# 2352
def equalPairs(grid: list[list[int]]) -> int:
    def convert_to_key(arr):
        return tuple(arr)
    
    rows = {}
    for row in grid:
        k = convert_to_key(row)
        rows[k] = rows.get(k, 0) + 1

    cols = {}
    for i in range(len(grid[0])):
        temp = []
        for j in range(len(grid)):
            temp.append(grid[j][i])
        
        k = convert_to_key(temp)
        cols[k] = cols.get(k, 0) + 1
    
    #print(rows)
    #print(cols)
    
    ans = 0
    for key in cols:
        #print(f"{key}: {rows.get(key)} | {cols.get(key)}")
        if rows.get(key) != None and cols.get(key) != None:
            ans += rows.get(key) * cols.get(key) 
            
    #print(ans)
    return ans
        
        
def numJewelsInStones(jewels: str, stones: str) -> int:
    
    jewel_set = set(jewels)
    #ans = [i for i in range(len(stones)) if stones[i] in jewel_set]
    ans = sum(stone in jewel_set for stone in stones)
   
    return ans
            
            

def main():
    jewels = "aA"
    stones = "aAAbbbb"
    print(numJewelsInStones(jewels, stones))
    
    #print(equalPairs(grid))
    #grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    #print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    #print(findMaxLength([0,1,0,0,1,1,0]))    
    #nums = [9,9,8,8]
    #print(largestUniqueNumber(nums))
    #res = findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])
    #print(res)
    #print(oddSubarray([1, 1, 2, 1, 1], 3))
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