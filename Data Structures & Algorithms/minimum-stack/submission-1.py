class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        if not self.stack:
            return None
        self.stack.pop()
        
    def top(self) -> int:
        item = self.stack[-1]
        return item
        self.stack.append(item)
    def getMin(self) -> int:
        minVal = self.stack[0]
        for val in self.stack:
            if val < minVal:
                minVal = val
        return minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()