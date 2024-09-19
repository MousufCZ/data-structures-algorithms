class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedChainHashMap:
    def __init__(self, size = 100):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
            print(f"if: {self.table}")
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)
            print(f"else: {self.table}")
    
    