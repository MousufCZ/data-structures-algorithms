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
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)
    
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    print(self.table[index])
                    self.table[index] = current.next
                return
            prev = current
            current = current.next

    def search(self, key):
        index = self.hash_function(key)
        key_search_count = 0
        current = self.table[index]
        print(f"Seeking table index on search: \n {current}")
        while current:
            if current.key == key: 
                return current.value, current.key
            current = current.next
            key_search_count =+ 1
            print(f"Current next to search key: \n{current}, \n Searched for key for a total of: {key_search_count} time, \n on this table[index]: {index}")
        return None