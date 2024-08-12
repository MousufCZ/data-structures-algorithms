from algorithms import algorithmBasics

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

algoClass = algorithmBasics.MaxProductTest()
output = algoClass.max_product(arr)
#output = algorithmBasics.swap_first_k_with_rest(arr, 3)


if __name__ == "__main__":
        print(f"...{output} ....")