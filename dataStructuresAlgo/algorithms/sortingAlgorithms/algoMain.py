from sequential_search import SequentialSearch

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    target = 6
    test = SequentialSearch()
    runFunction = test.sequentialSearch(list, target)
    print(runFunction)