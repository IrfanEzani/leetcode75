#!/usr/bin/env python3

from typing import List
from collections import Counter

'''
Example 1: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.

E.g. nums = [3, 1, 2, 7, 4, 2, 1, 1, 5] and k = 8.
'''

def longestSubarray(nums, k):
    left = sum = ans = 0
    
    for right in range(len(nums)):
        # add to sum using right ptr
        sum += nums[right]
        
        # when total sum > k
        while sum > k:
            #remove elem from left ptr
            sum -= nums[left]
            # move left ptr
            left += 1
        # update ans with the size of window
        # window size formula: r - l + 1
        ans = max(ans, right-left+1)
        
    return ans
    
'''
Problem 2: n of subarrays
Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
'''

def numSubarrays(nums : list[int], k: int) -> int:
    
    # base case:
    if k <= 1:
        return 0
    
    left = ans = 0
    
    # window
    curr = 1
    
    for right in range(len(nums)):
        curr *= nums[right]
        
        while curr > k:
            curr //= nums[left]
            left -= 1
        # add subarrays. length of window: n. of valid subarray
        ans += right - left + 1

'''
fixed window size
Problem 3: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
'''

def sumSubarray(nums: list[int], k: int) -> int:
    # 1. build window of size k
    curr = 0
    for i in range(k):
        curr += nums[i]
    
        
    # slide window down
    ans = curr
    for i in range(k, len(nums)):
        # add the one infront, remove the last one from behind
        curr += nums[i] - nums[i-k]
        # update max val
        ans = max(ans, curr)

def findMaxAverage(nums: list[int], k: int) -> float:
    
    curr = 0
    
    # build window until size k
    for i in range(k):
        print(nums[i])
        curr += nums[i]
        
    ans = curr / k
    print(f"curr ans: {ans}")
    
    # slide window size k until end of arr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i-k]
        ans = max(ans, curr / k)
    
    print(f"after loop answer: {ans}")
        
    
    """ 
    left = 1
    for i in range(left, len(nums) - k + 1):
        print(f"{i} subarray:")
        for j in range(k):
           print(nums[j+i])
     """    
        
    
        
    return ans

def longestOnesWithOneZero(nums: list[int]) -> int:
    left = curr = ans = 0
    for right in range(len(nums)):
        if nums[right] == '0':
            curr += 1
        
        while curr > 1:
            if nums[left] == '0':
                curr -= 1
            left += 1
            
        ans = max(ans, right - left + 1)
    return ans

def longestOnes(nums: List[int], k: int) -> int:
    left = curr = ans = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
            print(f"curr: {curr} ")
        
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        
        ans = max(ans, right-left+1)
    
    return ans

def minimumCardPickup(cards: list[int]) -> int: 
    
    last_seen = {}
    min_len = float('inf')
    
    for i, card in enumerate(cards):
        if card in last_seen:
            # here's the sliding window
            min_len = min(min_len, i - last_seen[card] + 1)
        # if not in dict, add card as key and its val as i
        last_seen[card] = i 

    return min_len if min_len != float('inf') else -1
            
    
def main():
    cards = [1,2,6,2,1]
    print(minimumCardPickup(cards))
    
if __name__ == "__main__":
    main()