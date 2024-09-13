class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insert_at_position(self, position, data):
        if position <= 0:
            self.insert_at_head(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(position - 1):
            if temp.next == self.head:
                break
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    
    def delete_at_head(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
    
    def delete_at_tail(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            prev = None
            while temp.next != self.head:
                prev = temp
                temp = temp.next
            prev.next = self.head
    
    def delete_at_position(self, position):
        if not self.head:
            return
        if position <= 0:
            self.delete_at_head()
            return
        temp = self.head
        prev = None
        for _ in range(position):
            prev = temp
            temp = temp.next
            if temp == self.head:
                return
        prev.next = temp.next

        