class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0
        
    def enqueue(self, data):
        self.queue.append(data)
        self.size += 1
        return data
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return_val = self.queue[0]
            del self.queue[0]
            self.size -= 1
            return return_val
        
    def top(self):
        return self.queue[0]
    
    def is_empty(self):
        return self.size == 0
