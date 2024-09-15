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
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_at_position(self, position, data):
        if position <= 0:
            self.insert_at_head(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current.next == self.head:
                break
            current = current.next
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_head(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
    
    def delete_at_tail(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
            prev.next = self.head
    
    def delete_at_position(self, position):
        if not self.head:
            # Check commit
            return
        if position <= 0:
            self.delete_at_head()
            return
        current = self.head
        prev = None
        for _ in range(position):
            prev = current
            current = current.next
            if current == self.head:
                return
        prev.next = current.next
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("None")