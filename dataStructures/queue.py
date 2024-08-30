class Queue:
    # Constructor to initialize the Queue with a given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def enqueue(self, item):
        if not self.isEmpty():
            self.queue.append(item)
            print(f'Enqueued: {item}')
        else:
            print('Queue is full')

    def dequeue(self):
        if not self.isEmpty():
            item = self.queue.pop(0)
            print(f'dequeue: {item}')
            return item
        else:
            print(f'Queue is empty. {self.queue}')

    def peek(self):
        if not self.isEmpty():
            print(f'Peak: {self.queue[0]}')
            return self.queue[0]
        else:
            print("Queue is empty.")

    def rear(self):
        if not self.isEmpty():
            print(f'Rear: {self.queue[-1]}')
            return self.queue[-1]
        else:
            print("Queue is empty.")

    def isFull(self):
        if len(self.queue) == self.capacity:    
            return 

    def isEmpty(self):
        if len(self.queue) == 0:
            return
    
def test_queue():                    # Function to test the Queue class
    # Create a queue with capacity 5
    q = Queue(5)

    # Enqueue some elements
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    # Try to enqueue when the queue is full
    q.enqueue(6)

    # Peek at the front element
    q.peek()

    # Check the rear element
    q.rear()

    # Dequeue some elements
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()

    # Try to dequeue when the queue is empty
    q.dequeue()

    # Check if the queue is empty
    print("Is queue empty?", q.isEmpty())

    # Check if the queue is full
    print("Is queue full?", q.isFull())

if __name__ == "__main__":
    test_queue()  # Call the test_queue function when the script is executed