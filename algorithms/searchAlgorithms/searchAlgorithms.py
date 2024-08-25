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
            
            # If the target is in the right half of mid
            elif arr[middle] < target:
                low = middle + 1
            
            # If the target is in the left half of mid 
            else:
                high = middle - 1
        
        return -1 # Target not found, return -1
    

    def binarySearchRecursive(self, arr, low, high, target):
        # Set the initial boundaries
        # low = 0
        # high = len(arr) - 1

        # Continue searching while the search space is valid
        while low <= high:
            # Calculate the middle index
            middle = (low + high) // 2


            # Check if the middle element is the target
            if arr[middle] == target:
                return middle
            
            # If the target is in the right half of mid
            elif arr[middle] < target:
                return BinarySearch.binarySearchRecursive(arr, middle - 1, high, target)
            
            # If the target is in the left half of mid 
            elif arr[middle] > target:
                return BinarySearch.binarySearchRecursive(arr, low, middle - 1, target)
            
        return -1 # Target not found
    
    def binarySearch(self, arr, low, high, x):
        # Check base case
        if high >= low:

            mid = low + (high - low) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it
            # can only be present in left subarray
            elif arr[mid] > x:
                return binarySearch(self, arr, low, mid-1, x)

            # Else the element can only be present
            # in right subarray
            else:
                return binarySearch(self, arr, mid + 1, high, x)

        # Element is not present in the array
        else:
            return -1