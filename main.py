from algorithms.searchAlgorithms import searchAlgorithms

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#randArr = [13, 4, 16, 8, 14, 5, 18, 11, 15, 2, 17, 12]

algoInstance = searchAlgorithms.BinarySearch()
target = 3

#b = searchAlgorithms.binarySearch(arr, 0, len(arr) -1, target)
output = algoInstance.binarySearch(arr, 0, len(arr) -1, target)

if __name__ == "__main__":
        print(f"Binary search: target number {target} is at element {b} in the array ....")