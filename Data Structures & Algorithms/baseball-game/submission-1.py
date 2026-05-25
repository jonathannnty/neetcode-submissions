from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # input is a list of strings
        # output is an integer
        non_int = '+DC'
        stack = deque()

        for operation in operations:
            if operation not in non_int:
                stack.append(int(operation))
                continue
            if operation == '+':
                prev = (stack.pop(), stack.pop())
                stack.append(prev[1])
                stack.append(prev[0])
                stack.append(prev[0] + prev[1])
            elif operation == 'D':
                prev = stack.pop()
                stack.append(prev)
                stack.append(prev * 2)
            else:
                stack.pop()
            print(f"after executing {operation}, this is the resulting stack: {stack}")
        print(stack)
        return sum(stack)
