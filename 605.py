def canPlaceFlowers(self, flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    
    res = True
    if n == 0:
        return res
    
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            print(f"replace index {i} ({flowerbed[i]}) with 1")
            n -= 1
            if n == 0:
                break
    
    
    if n > 0:
        res = False
        
    for i in flowerbed:
        print(i)
        
    return res
    
    
def main():
    flowerbed = [1,0,0,0,1]
    n = 1
    result = canPlaceFlowers(None, flowerbed, n)
    print(result)
    
    
if __name__ == "__main__":
        main()
        