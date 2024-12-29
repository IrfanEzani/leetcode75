def reverseWords(self, s: str) -> str:
    res = s.split()
    res.reverse()
    return " ".join(res) 

def main():
    result = reverseWords(None, "a good   example")
    print(result)
    
if __name__ == "__main__":
        main()