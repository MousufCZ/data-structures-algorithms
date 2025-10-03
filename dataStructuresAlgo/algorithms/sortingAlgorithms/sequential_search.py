# Sequential Search
class SequentialSearch:
    def sequentialSearch(self, array, target):
        index = 0
        while index < len(array) and array[index] != target:
            index = index + 1
        return index