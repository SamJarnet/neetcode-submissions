class MinStack:

    def __init__(self):
        self.stack = []
        self.head = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.head += 1

    def pop(self) -> None:
        self.stack.pop(self.head-1)
        self.head -= 1

    def top(self) -> int:
        return self.stack[self.head -1] 

    def getMin(self) -> int:
        return min(self.stack)
