class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2
    
    def leftChid(self, i):
        return 2 * i + 1
    
    def rightChild(self, i):
        return 2 * i + 2
    
    def insert(self, item):
        self.heap.append(item)
        self.heapifyUp(len(self.heap) - 1)
    
    def heapifyUp(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extractMin(self):
        if len(self.heap) == 0:
            return None
        
        minElement = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapifyDown(0)
        return minElement

    def heapifyDown(self, i):
        minIndex = i
        left = self.leftChid(i)
        right = self.rightChild(i)

        if left < len(self.heap) and self.heap[left] < self.heap[minIndex]:
            minIndex = left

        if right < len(self.heap) and self.heap[right] < self.heap[minIndex]:
            minIndex = right

        if i != minIndex:
            self.heap[i], self.heap[minIndex] = self.heap[minIndex], self.heap[i]
            self.heapifyDown(minIndex)

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None