class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            nextObj = (x, x)
        else:
            currObj = self.stack[len(self.stack)-1]

            if x < currObj[1]:
                nextObj = (x, x)
            else:
                nextObj = (x, currObj[1])

        self.stack.append(nextObj)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1][0]

    def getMin(self) -> int:
        lastPos = len(self.stack)-1
        return self.stack[lastPos][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3), print(obj)
obj.pop(), print(obj)
