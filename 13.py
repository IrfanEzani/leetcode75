def romanToInt(s: str) -> int:
    romans = {'I': 1, 'V':  5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(len(s)):
        if i+1 < (len(s)) and romans.get(s[i]) < romans.get(s[i+1]):
            res -= romans.get(s[i])
        else:
            res += romans.get(s[i]) 
            
    return res


def main():
    s = "MCMXCIV"
    print(romanToInt(s))
    pass

if __name__ == "__main__":
    main()