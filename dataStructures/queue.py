class Queue:
    # Constructor to initialize the Queue with a given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def enqueue(self, item):
        if len(self.queue) < self.capacity:
            self.queue.append(item)
            print(f'Enqueued: {item}')
        else:
            self.isFull()
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
        return len(self.queue) == self.capacity   

    def isEmpty(self):
        return len(self.queue) == 0