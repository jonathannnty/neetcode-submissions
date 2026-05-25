from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = "+-*/"
        # list of strings called tokens
        # output we want is an int
        # the result of executing a series of operands and operators in tokens

        # using a stack, as we add operands to the stack
        # when we encounter an operator
        # we're gonna pop out the two top-most elements in the stack
        # and execute the operator we encountered
        # afterwards the result is then added to this stack
        # this process continues until we should have a number at the end of iterating through
        # tokens

        stack = deque()

        for token in tokens:
            print(f"current stack: {stack}")
            if token in operator:
                val1 = stack.pop()
                val2 = stack.pop()
                print(f"popped 2 stack: {stack}, val1: {val1}, val2: {val2}, operation: {token}")

                # operations
                if token == "+":
                    stack.append(val1 + val2)
                elif token == "-":
                    stack.append(val2 - val1)
                elif token == "*":
                    stack.append(val1 * val2)
                else:
                    result = val2//val1 if val2//val1 > 0 else math.ceil(val2/val1)
                    stack.append(result)
                continue

            stack.append(int(token))
        return stack.pop()