from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_ = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

        min_top = self.min_[-1] if self.min_ else float("inf")
        self.min_.append(min(val, min_top))
        return

    def pop(self) -> None:
        self.min_.pop()
        self.stack.pop()

    def top(self) -> int:
        val = self.stack.pop()
        self.stack.append(val)
        return val

    def getMin(self) -> int:
        min_val = self.min_[-1] if self.min_ else None
        return min_val
