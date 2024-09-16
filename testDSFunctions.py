from dataStructures import queue
from dataStructures import stack
from dataStructures.heap import maxHeap
from dataStructures.heap import minHeap
from dataStructures.linkedList import singlyLinkedList
from dataStructures.linkedList import doublyLinkedList
from dataStructures.linkedList import circularLinkedList

def testStack():

        dsInstance = stack.Stack()
        currentStack = dsInstance.stack

        dsInstance.isEmpty(currentStack)
 
        dsInstance.push(1)
        dsInstance.push(2)
        dsInstance.push(3)
        dsInstance.push(4)

        dsInstance.isEmpty(currentStack)
        print(currentStack)

        dsInstance.pop(currentStack)
        print(currentStack)

        dsInstance.peek(currentStack)

def testQueue():                
        dsInstance = queue.Queue(5)
        dsInstance.enqueue(463)
        dsInstance.enqueue(243)
        print(dsInstance.queue)
        dsInstance.enqueue(2)
        dsInstance.enqueue(3)
        ## checking if queue is full by enqueuing more elements
        print(dsInstance.queue)
        dsInstance.dequeue()
        print(dsInstance.queue)
        dsInstance.peek()
        dsInstance.rear()
        print(f'Is queue empty?: {dsInstance.isEmpty()}')
        print(f'Is queue full?: {dsInstance.isFull()}')
 
def testMaxHeap():
        dsInstance = maxHeap.MaxHeap()

        dsInstance.insert(5)
        dsInstance.insert(3)
        dsInstance.insert(8)
        dsInstance.insert(1)
        dsInstance.insert(10)
        print(dsInstance.heap)
        
        print(f"peek: {dsInstance.peek()}")
        
        print(f"Extract Max: {dsInstance.extractMax()}")
        print(dsInstance.heap)

def testMinHeap():
        dsInstance = minHeap.MinHeap()
        dsInstance.insert(5)
        dsInstance.insert(3)
        dsInstance.insert(8)
        dsInstance.insert(1)
        dsInstance.insert(10)
        dsInstance.extractMin()
        print(dsInstance.heap)
        print(f'The heap peek is: {dsInstance.peek()}')

def testSinglyLinkedList():
        dsInstance = singlyLinkedList.SinglyLinkedList()
        dsInstance.append(2)
        dsInstance.traverseList()
        dsInstance.append(1)
        dsInstance.append(2)
        dsInstance.append(3)
        dsInstance.append(4)
        dsInstance.append(5)
        print("Original Linked List:")
        dsInstance.traverseList()  # Print the original linked list
        dsInstance.prepend(0)
        print("\nLinked List after prepending 0:")
        dsInstance.traverseList()  # Print the linked list after prepending
        dsInstance.insertAtPosition(2, 2.5)
        print("\nLinked List after inserting 2.5 at position 2:")
        dsInstance.traverseList()  # Print the linked list after inserting
        dsInstance.deleteNode(3)
        print("\nLinked List after deleting node with key 3:")
        dsInstance.traverseList() 

def testDoublyLinkedList():
        dsInstance = doublyLinkedList.DoublyLinkedList()
        dsInstance.insert_at_head(1)
        dsInstance.insert_at_head(2)
        dsInstance.insert_at_tail(3)
        dsInstance.traverse()
        dsInstance.insert_at_position(2, 4)
        dsInstance.traverse()
        dsInstance.delete_at_head()
        dsInstance.traverse()
        dsInstance.delete_at_tail()
        dsInstance.traverse()
        dsInstance.delete_at_position(0)
        dsInstance.traverse()
        
def testCircularLinkedList():
        dsInstance = circularLinkedList.CircularLinkedList()
        dsInstance.insert_at_head(1)
        dsInstance.insert_at_head(2)
        dsInstance.insert_at_tail(3)
        dsInstance.traverse()
        dsInstance.insert_at_position(2, 4)
        dsInstance.traverse()
        dsInstance.delete_at_head()
        dsInstance.traverse()
        dsInstance.delete_at_tail()
        dsInstance.traverse()
        dsInstance.delete_at_position(1)
        dsInstance.traverse()