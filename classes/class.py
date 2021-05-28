class nodeLinkedList:
    def __init__(self, data=None, Next=None):
        self.data = data
        self.Next = Next
        
class myLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, data):
        """
        Add a node to the head of the linked list
        """
        new_node = nodeLinkedList(data)
        if self.head != None:
            new_node.Next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        
        
    def add_last(self, data):
        """
        Add a node to the end of the linked list
        """
        if self.head == None:
            self.head = nodeLinkedList(data)
            self.tail = self.head
            return
        else:
            self.tail.Next = nodeLinkedList(data)
            self.tail = self.tail.Next

    def remove_first(self):
        """
        Remove the first node of the linked list
        """
        if self.head == None:
            pass
        elif self.head.Next == None:
            self.head = None
        else:
            first = self.head
            self.head = self.head.Next
            return first
    
    def remove_last(self):
        """
        Remove the last node of the linked list
        """
        if self.head == None:
            pass
        elif self.head.Next == None:
            self.head = None
        else:
            second_last = self.head
            while(second_last.Next.Next):
                second_last = second_last.Next
            second_last.Next = None
    def list_traversal(self):
        """
        Traverse the linked list, printing each node's value
        """
        if self.head == None:
            print("Empty Linked List")
        else:
            temp_node = self.head
            while temp_node != None:
                print(temp_node.data)
                temp_node = temp_node.Next
                
    def search(self, search_val):
        """
        Traverse the linked list, if a node with 
        data = value of the search_val return True
        """
        if self.head != None:
            temp_node = self.head
            while temp_node != None:
                if temp_node.data == search_val:
                    return True
                temp_node = temp_node.Next
        return False
    
    def to_list(self):
        """
        Traverse linked list returns list object with LL values
        """
        ll_list = []
        temp_node = self.head
        while temp_node != None:
            ll_list.append(temp_node.data)
            temp_node = temp_node.Next
        return ll_list
    
    
    
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
            self.stack = self.stack[:-1]
            self.size -= 1
            return popped_val
    
    def top(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[-1]
        
    def is_empty(self):
        return self.size == 0
    
    
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
            self.queue = self.queue[1:]
            self.size -= 1
            return return_val
        
    def top(self):
        return self.queue[0]
    
    def is_empty(self):
        return self.size == 0

    
    
class StackLL:
    def __init__(self):
        self.Stack = myLinkedList()
        self.size = 0

    def push(self, data):
        self.Stack.add_first(data)
        self.size += 1
        return data

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            popped_val = self.Stack.remove_first()
            self.size -= 1
            return popped_val
    
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
            return -1
        else:
            return self.Stack.head.data
        
    def is_empty(self):
        return self.size == 0
    
class QueueLL:
    def __init__(self):
        self.queue = myLinkedList()
        self.size = 0
        
    def enqueue(self, data):
        self.queue.add_first(data)
        self.size += 1
        return data
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return_val = self.queue.tail
            self.queue.remove_last()
            self.size -= 1
            return return_val
        
    def top(self):
        return self.queue.head.data
    
    def is_empty(self):
        return self.size == 0