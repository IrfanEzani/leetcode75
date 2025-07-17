def reverseOnlyLetters(s: str) -> str:
    letters = [c for c in s if c.isalpha()]
    ans = []
    for i in s:
        if i.isalpha():
            ans.append(letters.pop())
        else:
            ans.append(i)
            
    
    return "".join(ans)

def main():
    s = "a-bC-dEf-ghIj"
    res = reverseOnlyLetters(s)
    print(res)

if __name__ == "__main__":
    main()