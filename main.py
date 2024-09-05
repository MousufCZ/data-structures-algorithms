from dataStructures import queue
from dataStructures import stack
from dataStructures import maxHeap
from dataStructures import minHeap
from dataStructures import singlyLinkedList

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
        ll = singlyLinkedList.SinglyLinkedList()
        ll.append(2)
        ll.traverseList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        print("Original Linked List:")
        ll.traverseList()  # Print the original linked list
        ll.prepend(0)
        print("\nLinked List after prepending 0:")
        ll.traverseList()  # Print the linked list after prepending
        ll.insertAtPosition(2, 2.5)
        print("\nLinked List after inserting 2.5 at position 2:")
        ll.traverseList()  # Print the linked list after inserting
        ll.deleteNode(3)
        print("\nLinked List after deleting node with key 3:")
        ll.traverseList() 

if __name__ == "__main__":
        testSinglyLinkedList()