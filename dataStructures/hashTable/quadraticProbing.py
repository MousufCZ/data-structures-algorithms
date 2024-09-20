""" 
Quadratic probing implemented differently from Linked Chain.
It isn't using node based bapping using 'Table', but creating
individual mapping for 'Keys' and 'Values'
"""
class QuadraticProbingOpenAddressing:
    def __init__(self, size=100):
        self.size = size
        self.keys = [None] * self.size  # Array to store keys
        self.values = [None] * self.size  # Array to store values

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)  # Get the initial index using the hash function
        offset = 1  # Initialize the quadratic probing offset
        while self.keys[index] is not None:  # Continue until an empty slot is found
            index = (index + offset ** 2) % self.size  # Quadratic probing for the next index
            offset += 1  # Increment the offset for the next iteration
        self.keys[index] = key  # Insert the key into the keys array
        self.values[index] = value  # Insert the corresponding value into the values array

    def delete(self, key):
        index = self._hash_function(key)  # Get the initial index using the hash function
        offset = 1  # Initialize the quadratic probing offset
        while self.keys[index] is not None:  # Continue until an empty slot is found
            if self.keys[index] == key:  # Check if the key matches
                self.keys[index] = None  # Set the key to None to delete it
                self.values[index] = None  # Set the corresponding value to None
                return  # Exit the function after deletion
            index = (index + offset ** 2) % self.size  # Quadratic probing for the next index
            offset += 1  # Increment the offset for the next iteration

    def search(self, key):
        index = self._hash_function(key)  # Get the initial index using the hash function
        offset = 1  # Initialize the quadratic probing offset
        while self.keys[index] is not None:  # Continue until an empty slot is found
            if self.keys[index] == key:  # Check if the key matches
                return self.values[index]  # Return the corresponding value
            index = (index + offset ** 2) % self.size  # Quadratic probing for the next index
            offset += 1  # Increment the offset for the next iteration
        return None  # Return None if the key is not found