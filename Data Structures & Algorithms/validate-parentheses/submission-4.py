from collections import deque

class Solution:
    

    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        pairs = {'(':')', '[':']', '{':'}'}
        opening = pairs.keys()
        stack = deque()

        for c in s:
            print(f"stack: {stack}")
            if c in opening:
                stack.append(c)
                continue
            if len(stack) > 0 and pairs[stack[len(stack) - 1]] == c:
                stack.pop()
            else:
                return False
        return True if len(stack) == 0 else False