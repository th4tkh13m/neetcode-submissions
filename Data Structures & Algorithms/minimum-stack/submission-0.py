class MinStack:

    def __init__(self):
        # maybe we do doubly linked list
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        # Add but update min val
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
            self.min.append(val)
        else:
            current_min = self.min[-1]
            self.min.append(val)
            if val < current_min:
                self.min.append(val)
            else:
                self.min.append(current_min)

    def pop(self) -> None:
        # Remove and update min val
        self.stack.pop()
        self.min.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
        

    def getMin(self) -> int:
        return self.min[-1]

