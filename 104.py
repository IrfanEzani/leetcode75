def removeDuplicates(s: str) -> str:
   stack = []
   
   for char in s:
       # if stack is not empty and the last element is same as curr
        if stack and stack[-1] == char:
           stack.pop()
        else:
            stack.append(char)
   
   return "".join(stack)

def main():
    # Your code here
    s = "abbaca"
    print(removeDuplicates(s))
    pass

if __name__ == "__main__":
    main()
    