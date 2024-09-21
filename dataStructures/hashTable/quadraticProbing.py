""" 
Quadratic probing implemented differently from Linked Chain.
It isn't using node based bapping using 'Table', but creating
individual mapping for 'Keys' and 'Values'
"""
class QuadraticProbingOpenAddressing:
    def __init__(self, size=100):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        offset = 1
        while self.keys[index] is not None:
            index = (index + offset ** 2) % self.size
            offset += 1
        self.keys[index] = key
        self.values[index] = value

    def delete(self, key):
        index = self._hash_function(key)
        offset = 1
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return
            index = (index + offset ** 2) % self.size
            offset += 1

    def search(self, key):
        index = self._hash_function(key)
        offset = 1
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + offset ** 2) % self.size
            offset += 1
        return None