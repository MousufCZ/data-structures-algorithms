from algorithms import algorithmBasics
from algorithms import sortingAlgorithms

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#algoClass = algorithmBasics.MaxProductTest()
#output = algoClass.max_product(arr)
#output = algorithmBasics.swap_first_k_with_rest(arr, 3)
output = sortingAlgorithms.fisher_yates_shuffle(arr)

if __name__ == "__main__":
        print(f"...{arr} ....")