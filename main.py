from dataStructures import queue

def testQueue():                
        dsInstance = queue.Queue(5)
        dsInstance.enqueue(463)
        dsInstance.enqueue(243)
        print(dsInstance.queue)
        dsInstance.enqueue(2)
        dsInstance.enqueue(3)
        dsInstance.enqueue(3)
        # checking if queue is full
        dsInstance.enqueue(3)
        dsInstance.enqueue(3)
        dsInstance.enqueue(3)
        dsInstance.enqueue(3)

        print(dsInstance.queue)
        #dsInstance.dequeue()
        print(dsInstance.queue)
        dsInstance.peek()
        dsInstance.rear()
        print(f'Is queue empty?: {dsInstance.isEmpty()}')
        print(f'Is queue full?: {dsInstance.isFull()}')

if __name__ == "__main__":
        testQueue()