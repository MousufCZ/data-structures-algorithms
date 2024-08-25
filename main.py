from algorithms.searchAlgorithms import searchAlgorithms

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#randArr = [13, 4, 16, 8, 14, 5, 18, 11, 15, 2, 17, 12]

algoInstance = searchAlgorithms.BinarySearch()
target = 3

#b = searchAlgorithms.binarySearch(arr, 0, len(arr) -1, target)
output = algoInstance.binarySearchRecursive(arr, 0, len(arr) -1, target)

"""
The output for BinarySearch().binarySearch works correctly and returns element 2
correctly however BinarySearch().binarySearchRecursive calls the wrong element as -1.
I think there is a code mistake, have a look and fix.
"""

if __name__ == "__main__":
        print(f"Binary search: target number {target} is at element {output} in the array ....")