def reverseVowels(self, s: str) -> str:
    vowels = "aeiouAEIOU"
    s = list(s) # convert string to list to make it mutable
    i, j = 0, len(s) - 1 # two pointers
    
    # swaps the vowels
    while i < j:
        if s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    
    return "".join(s)
    

def main():
    result = reverseVowels(None, "IceCreAm")
    print(result)
    
    
if __name__ == "__main__":
        main()