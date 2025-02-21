class MinStack:
    def __init__(self):
        self.st = []
        self.curr_min = None

    def push(self, val: int) -> None:
        if len(self.st) == 0:
            self.curr_min = val
        elif val <= self.curr_min:
            self.curr_min = val

        self.st.append((val, self.curr_min))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-10)
obj.push(-14)
obj.getMin()
obj.getMin()
obj.push(-20)
obj.getMin()
obj.getMin()
obj.top()
obj.getMin()
obj.pop()
obj.push(10)
obj.push(-7)
obj.getMin()
obj.push(-7)
obj.pop()
obj.top()
obj.getMin()
obj.pop()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
