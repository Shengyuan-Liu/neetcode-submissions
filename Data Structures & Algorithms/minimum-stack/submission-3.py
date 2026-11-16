class MinStack:

    def __init__(self):
        self.data = []
        self.current_min = float('inf')
        

    def push(self, val: int) -> None:
        if val < self.current_min:
            self.current_min = val
        self.data.append((val, self.current_min))

    def pop(self) -> None:
        self.data.pop()
        if self.data:
            self.current_min = self.getMin()
        else:
            self.current_min = float('inf')
        

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]
        
# [(1, 1), (2, 1), (0, 0)]