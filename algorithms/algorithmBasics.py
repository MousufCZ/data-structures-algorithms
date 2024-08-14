def swap_first_k_with_rest(arr, k):
    if k <= 0 or k >= len(arr):
        print("Invalid value of k.")
        return arr

    # Reverse the first k elements
    arr[:k] = arr[:k][::-1]

    # Reverse the rest of the array
    arr[k:] = arr[k:][::-1]

    # Reverse the entire array
    arr.reverse()

    return arr


class MaxProductTest:
    def max_product(self, a):
        i = 0
        max = 0
        
        while i < len(a):
            j = i + 1
            while j < len(a):
                if a[i] * a[j] > max:
                    max = a[i] * a[j]
                j = j + 1
            i = i + 1
        return max
    
def find_largest_element(arr):
    # Assuming the array has at least one element
    max_element = arr[0]

    for num in arr[1:]:
        if num > max_element:
            max_element = num

    return max_element


class CountZero:
    def foo(self, a):
        count = 0
        i = 0
        while i < len(a):
            if a[i] == 0:
                count += 1
            i += 1
        return count


def reverse_subrange(arr, lower_index, upper_index):
    # Check for valid indices
    if lower_index < 0 or upper_index >= len(arr) or lower_index > upper_index:
        print("Invalid indices.")
        return arr

    # Reverse the subrange
    while lower_index < upper_index:
        arr[lower_index], arr[upper_index] = arr[upper_index], arr[lower_index]
        lower_index += 1
        upper_index -= 1
    return arr
