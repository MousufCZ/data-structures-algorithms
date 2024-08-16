from algorithms import algorithmBasics
from algorithms.sortingAlgorithms import sortingAlgorithms

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
randArr = [13, 4, 16, 8, 14, 5, 18, 11, 15, 2, 17, 12]

algoInstance = sortingAlgorithms.InsertionSort()
output = algoInstance.insertionSort(randArr) 

if __name__ == "__main__":
        print(f"Sort algorith check: {randArr} ....")