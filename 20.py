class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {"(":")", "{":"}", "[":"]"}
        
        for bracket in s:
            # if an opening bracket is in the dict
            if bracket in matches:
                stack.append(bracket)
            else:
                # if stack is empty, i.e. no matching bracket found, return false
                if not stack:
                    return False
                
                # pop most recent bracket
                previous = stack.pop()
                # if the value doesn't match, return False, else move on.
                if matches[bracket] != previous:
                    return False
        
        return not stack
                