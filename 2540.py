
def getCommon(nums1: list[int], nums2: list[int]) -> int:
    i1 = i2 = 0
    while i1 < len(nums1) and i2 < len(nums2):
        if nums1[i1] < nums2[i2]:
            i1 += 1
        elif nums1[i1] > nums2[i2]:
            i2 += 1
        else:
            return nums1[i1]
    return -1

def main():
    nums1 = [1,2,8,12,32,34,43,52,57,62,64,67,71,71,79,81,86,91,93,94]
    nums2 = [9,11,12,14,19,25,29,31,38,39,41,42,58,63,66,70,71,73,91,91]
    print(getCommon(nums1, nums2))
    pass

if __name__ == "__main__":
    main()
    
    