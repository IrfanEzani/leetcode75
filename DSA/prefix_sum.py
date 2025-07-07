#!/usr/bin/env python3

def prefixSum(nums: list[int]) -> list[int]:
    # init with first elem
    res = [nums[0]]
    
    # iterate from second to last, add nums[i] with last res elem.
    for i in range(1, len(nums)):
        res.append(nums[i] + res[-1])
        
    return res


'''
Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
'''

def answer_queries(nums, queries, limit):
    # get prefix arr
    prefix = [nums[0]]
    
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    res = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        res.append(curr < limit)
    
    return res

'''
Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.
'''
def waysToSplitArray(nums: list[int]) -> int:
    n = len(nums)
    
    prefix = [nums[0]]
    for i in range(1, n):
        prefix.append(nums[i] + prefix[-1])
    
    count = 0
    # split until last elem, if we go over, we cant split anything.
    for i in range(n-1):
        print(f"val i: {i}")
        left = prefix[i]
        # right: (last prefix - i) to get sum of i+1 until last elem
        right = prefix[-1] - prefix[i]
        if left >= right:
            count += 1
    
    return count

def splitArrayElegant(nums: list[int]) -> int:
    # to get left section, we can calculate the sum on-the-fly
    # to get right section, get sum of nums - left section
    # this allows for O(1) space complexity
    
    ans = left = 0
    total = sum(nums)
    
    for i in range(len(nums)-1):
        left += nums[i]
        right = total - left
        if left >= right:
            ans += 1


def minStartValue(nums: list[int]) -> int:
    
    curr = ans = 1
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    print(min(prefix)) # this is the minimum step by step
        
    for i in range(len(nums)):
        if abs(prefix[i]) >= curr:
            print(f"curr: {curr}, prefix[i]: {prefix[i]}")
            curr = abs(prefix[i]) + 1
        ans = max(ans, curr)
            
    # we can also do this: return 1 - min(prefix)
    # derived from : minStep + startValue = 1
    # startValue = 1 - minStep    
    return ans


'''
# A more elegant solution to the prev problem:
# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/editorial

 iterate over the array using startValue = 0, find the minimum step-by-step total in this iteration (say minVal), according to the previous proof, we should have minVal + startValue = 1, which is exactly startValue = 1 - minVal.
'''
def minStartValue(nums: list[int]) -> int:
    # "total": current step-by-step sum
    # "min_val" for minimum  step-by-step total among all sums.
    min_val = 0
    total = 0
    # Iterate over the array and get the minimum step-by-step total.
    for num in nums:
        total += num
        min_val = min(min_val, total)
    
    # We have to change the minimum step-by-step total to 1, 
    # by increasing the startValue from 0 to -min_val + 1, 
    # which is just the minimum startValue we want.
    return 1 - min_val

def getAverages(nums: list[int], k: int) -> list[int]:
    # prefix array
    pref = [nums[0]]
    for i in range(1, len(nums)):
        pref.append(nums[i] + pref[-1])
    
    
    res = [0] * len(nums)
    
    for i in range(len(nums)):
        if i < k or len(nums) - i - 1 < k:
            res[i] = -1
        else:
            left = i - k
            right = i + k
            sub_arr = pref[right] - pref[left] + nums[left]
            n = 2*k + 1
            res[i] = int(sub_arr / n)        
    return res
    
def main():
    nums = [8]
    k = 100
    getAverages(nums, k)


if __name__ == "__main__":
    main()