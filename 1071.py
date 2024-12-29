def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        return str1[:gcd(len(str1), len(str2))]
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        
        
def main():
    str1 = "ABCABC"
    str2 = "ABC"
    result = gcdOfStrings(None, str1, str2)
    print(result)
    
    
if __name__ == "__main__":
        main()