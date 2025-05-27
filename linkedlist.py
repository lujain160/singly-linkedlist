from node import Node
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_front(self,data):
        newNode=Node(data) 
        if self.head is not None:
            newNode.next=self.head
        self.head=newNode
    def insert_at_end(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode      
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newNode
    def insert_after(self,previous_node,data):
        if previous_node is None:
            return
        newNode=Node(data)
        newNode.next=previous_node.next
        previous_node.next = newNode
    def get_first_node(self):
        return self.head
    def get_last_node(self):
        if self.head is None:
            return
        current=self.head
        while current.next is not None:
                current=current.next
        return current                        
    def get_node(self,data):
        current=self.head
        while current is not None:
            if current.data==data:
                return current
            current=current.next
        return None    
    def delete_node(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        prev=None
        while current is not None and current.data !=data:
            prev=current
            current=current.next
        if current is None:
            return
        prev.next=current.next 
    def print_list(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next
        print()           
