class SequentialSearch:
    def sequentialSearch(self, arr, target):
        i = 0
        while i < len(arr) and arr[i] != target:
            i = i + 1
        return i