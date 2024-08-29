class Queue:
    # Constructor to initialize the Queue with a given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def enqeue(self, item):
        if len(self.queue) < self.capacity:
            self.queue.append(item)
            print(f'Enqueued: {item}')
        else:
            print('Queue is full')


    def isFull(self):
        return print(f'Queue is full. {len(self.queue) == self.capacity}')

    def isEmpty(self):
        return (f'Queue is empty. {len(self.queue) == 0}')