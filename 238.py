from typing import List

def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    print(res)
    return res
        
def main():
    nums = [-1,1,0,-3,3]
    productExceptSelf(None, nums)
    
if __name__ == "__main__":
        main()