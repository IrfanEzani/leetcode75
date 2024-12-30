from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    res = False
    
    first = second = float('inf')
    
    for n in nums:
        # if n <= first smallest number
        if n <= first:
            first = n 
        # if n > first smallest number, but <= second
        elif n <= second:
            second = n  
        #  if n > first and second
        else:
            res = True  
            break
    
    return res

""" 
sorting wouldn't work because it fails the condition of i < j < k of the original array

"""

def main():
    a = increasingTriplet([20,100,10,12,5,13])
    print(a)
    
if __name__ == "__main__":
    main()