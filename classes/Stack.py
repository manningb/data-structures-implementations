class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, data):
        self.stack.append(data)
        self.size += 1
        return data

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            popped_val = self.stack[-1]
            del self.stack[-1]
            self.size -= 1
            return popped_val
    
    def top(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[-1]
        
    def is_empty(self):
        return self.size == 0
