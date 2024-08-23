from algorithms.searchAlgorithms import searchAlgorithms

#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
randArr = [13, 4, 16, 8, 14, 5, 18, 11, 15, 2, 17, 12]

algoInstance = searchAlgorithms.SequentialSearch()
target = 15
output = algoInstance.sequentialSearch(randArr, target)

if __name__ == "__main__":
        print(f"Sequential search: target number {target} is at element {output} in the array ....")