class MinStack:
    # 考點：如何讓 getMin() 也可以 O(1)!

    def __init__(self):
        self.stack = []
        self.minstack = [] # 存到目前這個數為止的最小值      

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack:
            self.minstack.append(val)
        else:
            curmin = min(val, self.minstack[-1])
            self.minstack.append(curmin)
       
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
