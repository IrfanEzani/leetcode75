def backspaceCompare(s: str, t: str) -> bool:
    def build(s):
        stack = []
        for i in s:
            if i == '#':
                stack.pop()
            else:
                stack.append(i)
                
        return "".join(stack)
    
    return build(s) == build(t)
def main():
    # Your code here
    s = "a#c"
    t = "b"
    print(backspaceCompare(s,t))
    pass

if __name__ == "__main__":
    main()
    