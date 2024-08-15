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
