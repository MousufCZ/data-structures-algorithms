import random

# Sequential Search
class sequentialSearch:
    def sequentialSearch(self, a, x):
        i = 0
        while i < len(a) and a[i] != x:
            i = i + 1
        return i


# Fisher-Yates Shuffle Algorithm
def fisher_yates_shuffle(arr):
    n = len(arr)
    for i in range(n- 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        j = random.randint(0, i)
        # Swap the current element with the randomly selected element
        arr[i], arr[j] = arr[j], arr[i]


# Selection Sort Algorithm
class selectionSort:
    #@staticmethod  
    def selectionSort(self, arr):
        n = len(arr)
        
        for i in range(n - 1):
            min_index = i

            # Find the index of the minimum element in the unsorted part
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # Swap the minimum element with the first unsorted element
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion sort algorithm
class InsertionSort:
    def insertionSort (self, arr): 
        # Get the length of the array
        n = len(arr)

        # Iterate through each element in the array starting from the second element
        for i in range(1, n):
            # Select the current element as the "key"
            key = arr[i]
            # Set a variable "j" to the index before the current element
            j = i - 1

            # Compare and shift elements in the sorted portion to find the correct position for the current element
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j = j - 1

            # Place the key at its correct position in the sorted part
            arr[j + 1] = key

# ============================
# Divide and conqure sorting
# Quick sort and Merge sort
# ============================

# Quick sort

class QuickSort:
    def quickSort(self, arr, low, high):
        # Recursive quicksort function
        if low < high:
            # Partition the array and get the pivot's final position
            s = self.partition(arr, low, high)

            # Recursively sort the sub-arrays on both sides of the pivot
            #left of mid-point
            self.quickSort(arr, low, s - 1)
            self.quickSort(arr, s + 1, high)

        # Return the sorted array
        return arr

    def partition(self, arr, low, high):
        # Choose the pivot (the first element in the array)
        pivot = arr[low]

        # Initialize pointers for the left and right sides of the partition
        i = low + 1
        j = high 

        # Perform the partitioning
        while i <= j:
            # Find an element greater than the pivot on the left
            while i <= j and arr[i] <= pivot:
                i += 1

            # Find an element smaller than the pivot on the right
            while j >= i and arr[j] >= pivot:
                j -= 1

            # Swap elements to correct their positions
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j-= 1
            
        # Swap the pivot with the element at the final position
        arr[low], arr[j] = arr[j], arr[low]

        # Return the final position of the pivot
        return j