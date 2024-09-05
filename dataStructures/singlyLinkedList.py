class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
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
        
        prevNode = None
        
        while currentNode and currentNode.data != key:
            prevNode = currentNode
            currentNode = currentNode.next

        if currentNode is None:
            return
        
        prevNode.next = currentNode.next

    def traverseList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("End of List")