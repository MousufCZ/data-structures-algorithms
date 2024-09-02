from dataStructures import queue
from dataStructures import stack
from dataStructures import heap

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
 
def testHeap():
        dsInstance = heap.MaxHeap()

        dsInstance.insert(5)
        dsInstance.insert(3)
        dsInstance.insert(8)
        dsInstance.insert(1)
        dsInstance.insert(10)
        print(dsInstance.heap)
        
        print(f"peek: {dsInstance.peek()}")
        
        print(f"Extract Max: {dsInstance.extractMax()}")
        print(dsInstance.heap)


if __name__ == "__main__":
        testHeap()