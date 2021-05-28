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
