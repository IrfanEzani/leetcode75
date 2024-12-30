def isSubsequence(s: str, t: str) -> bool:
    j = 0
    s_list = list(s)
    
    if s == "": 
        return True
    if t == "" and s:
        return False
    
    for i in range(len(t)):
        if t[i] == s[j]:
            s_list.pop(0)
            j+=1
            if not s_list:
                break
    
    #print(f"s_list: {s_list}")
    
    return (len(s_list) == 0)


    # other solutions
    """ 
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
    
    """

def main():
    print(isSubsequence("abc", "ahbgdc")) # True
    print(isSubsequence("axc", "ahbgdc")) # False
    print(isSubsequence("", "ahbgdc")) # True
    print(isSubsequence("abc", "")) # False
    print(isSubsequence("", "")) # True
    
if __name__ == "__main__":
    main()