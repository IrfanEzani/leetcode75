from typing import List


def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1       
                    
        print(nums)
        
def main():
    nums = [0,1,0,3,12]
    moveZeroes(None, nums)
    
if __name__ == "__main__":
        main()