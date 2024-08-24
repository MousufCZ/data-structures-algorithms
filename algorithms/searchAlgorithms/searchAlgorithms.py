class SequentialSearch:
    def sequentialSearch(self, arr, target):
        i = 0
        while i < len(arr) and arr[i] != target:
            i = i + 1
        return i

# Binary search
class BinarySearch:
    def binarySearchLinear(self, arr, target):
        # Set the initial search boundaries
        low = 0
        high = len(arr) - 1

        # Continue searching while the search space is valid
        while low <= high:
            # Calculate the middle index
            middle = (low + high) // 2

            # Check if the middle element is the target
            if arr[middle] == target:
                return middle # Target found, return the index 
            
            # If the target is in the right half
            elif arr[middle] < target:
                low = middle + 1
            
            # If the target is in the left 
            else:
                high = middle - 1
        
        return -1 # Target not found, return -1