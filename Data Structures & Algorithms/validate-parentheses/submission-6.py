from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        opening = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in '({[':
                stack.append(c)
                continue
            if not stack or stack.pop() != opening[c]:
                return False
        
        return True if len(stack) == 0 else False

        