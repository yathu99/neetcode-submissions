class MinStack:

    def __init__(self):
        self.stack=[]
        self.last_min=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(self.last_min):
            self.last_min.append(min(self.last_min[-1],val))
        else:
            self.last_min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.last_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.last_min[-1]
