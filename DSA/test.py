#!/usr/bin/env python3
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        start = 0
        end = len(s) - 1
        temp = ''
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            
            end -= 1
            start += 1
        """
        
        start, end = 0, len(s) - 1
        
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums) - 1
        res = [0] * len(nums)
        # id to iterate over res arr
        idx = len(nums) - 1
        
        while start <= end:
            # use abs to compare magnitude
            if abs(nums[start]) > abs(nums[end]):
                # we load res arr from the back 
                res[idx] = nums[start] * nums[start]
                start += 1
            else:
                res[idx] = nums[end] * nums[end]
                end -= 1
            idx -= 1
            
        return res

def main():
    s = ["h","e","l","l","o"]
    Solution().reverseString(s)
    
    nums = [-4,-1,0,3,10]
    res = Solution().sortedSquares(nums)
    print(res)
    
if __name__ == "__main__":
    main()
