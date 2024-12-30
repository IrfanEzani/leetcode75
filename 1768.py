def mergeAlternately(word1, word2):
    res = ""
    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            res += word1[i]
        if i < len(word2):
            res += word2[i]
        
    return res

def main():
    a = mergeAlternately("abc", "pqr")
    print(a)

if __name__ == "__main__":
    main()