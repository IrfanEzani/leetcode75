
from collections import Counter


def longestCommonPrefix(strs: list[str]) -> str:
    
    # edge case
    if len(strs) == 0:
        return ""
    
    prefix = strs[0]
    
    for i in range(1, len(strs)):
        print(f"strs[i]: {strs[i]}")
        print(f"prefix: {prefix}")
        print(f"Outside, {strs[i]}.find({prefix}): {strs[i].find(prefix)}")
        while(strs[i].find(prefix) != 0):
            prefix = prefix[0: len(prefix) - 1]
            print(prefix)
            print(f"{strs[i]}.find({prefix}): {strs[i].find(prefix)}")
            
    return prefix
    
def main():
    strs = ["flower","flow","floght"]
    longestCommonPrefix(strs)
    
    #str1 = "flower"
    #str2 = "flow"
    #x = str1.find(str2)
    #print(x)
    pass

if __name__ == "__main__":
    main()