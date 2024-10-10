""" 
Linear probing implemented differently from Linked Chain.
It isn't using node based bapping using 'Table', but creating
individual mapping for 'Keys' and 'Values'
"""
class LinearProbingOpenAddressing:
    def __init__(self, size=100):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    def delete(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return
            index = (index + 1) % self.size

    def search(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None