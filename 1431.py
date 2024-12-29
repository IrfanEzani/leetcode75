# 1431. Kids With the Greatest Number of Candies
def kidsWithCandies(self, candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
        
    booleanCandies = []
    max = candies[0]
    for i in range(1, len(candies)):
        if candies[i] > max:
            max = candies[i]
    for i in range(len(candies)):
        booleanCandies.append(candies[i] + extraCandies >= max)
         

def main():
    candies = [12,1,12]
    extraCandies = 10
    result = kidsWithCandies(None, candies, extraCandies)
    print(result)
if __name__ == "__main__":
        main()