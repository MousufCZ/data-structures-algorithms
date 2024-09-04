class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

        def prepend(self, data):
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

        def insertAtPosition(self, position, data):
            if position == 0:
                self.prepend(data)
                return
            
            newNode = Node(data)
            currentNode = self.head
            prevNode = None
            currentPosition = 0

            while currentNode and currentPosition < position:
                prevNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1
            prevNode.next = newNode
            newNode.next = currentNode
            
            def deleteNode(self, key):
                currentNode = self.head
                if currentNode and currentNode.data == key:
                    self.head = currentNode.next
                    currentNode = None
                    return
# ============================