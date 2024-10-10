# Search algo


*   Binary search
*   List item



#Sequential search (Lecture 2)
Sequential search, also known as linear search, is a simple method for finding a specific value in a list or array. The search starts from the beginning of the list and proceeds sequentially through each element until a match is found or the entire list has been traversed. It works well for both ordered and unordered lists.

## Pseudocode
This pseudocode reflects the structure and logic of the provided Java code. It describes the class SequentialSearch with the sequential_search method and the main block for creating an instance, defining an array, calling the method, and printing the result. Pseudocode is a high-level description of the algorithm's logic, not tied to the syntax of any specific programming language.

class SequentialSearch:
    function sequential_search(a, x):
        i = 0
        while i < length(a) and a[i] != x:
            i = i + 1
        return i

if __name__ == "__main__":
    seq_search = create SequentialSearch instance
    data = [3, 7, 1, 9, 4, 6, 2, 8, 5]
    target = 6

    result = seq_search.sequential_search(data, target)
    print "Index of", target, "in the array:", result

    # Binary search (Lecture 5)

## Time complexity
O(log n)

## Pseudocode

```
function binarySearch(arr, target):
    // Set the initial search boundaries
    lo = 0
    hi = length(arr) - 1

    // Continue searching while the search space is valid
    while lo <= hi:
        // Calculate the middle index
        mid = (lo + hi) / 2

        // Check if the middle element is the target
        if arr[mid] == target:
            return mid  // Target found, return the index

        // If the target is in the left half
        if arr[mid] < target:
            lo = mid + 1
        // If the target is in the right half
        else:
            hi = mid - 1

    return -1  // Target not found, return -1
```

# Binary search (Lecture 5)

## Time complexity
O(log n)

## Pseudocode

```
function binarySearch(arr, target):
    // Set the initial search boundaries
    lo = 0
    hi = length(arr) - 1

    // Continue searching while the search space is valid
    while lo <= hi:
        // Calculate the middle index
        mid = (lo + hi) / 2

        // Check if the middle element is the target
        if arr[mid] == target:
            return mid  // Target found, return the index

        // If the target is in the left half
        if arr[mid] < target:
            lo = mid + 1
        // If the target is in the right half
        else:
            hi = mid - 1

    return -1  // Target not found, return -1
```




## Pattern
Question: what is the key pattern of the code in once sentence? This pattern should be a distinctive feature of the code which can trigger a memory for me when trying to recall the code.

Answer: The key pattern in the binary search code is the iterative halving of the search space based on comparisons with the middle element, ensuring efficient exploration of sorted data.


##Why

Binary search is a highly efficient algorithm for finding a specific target element in a sorted collection, and its use is justified in several scenarios:

1. **Efficiency:**
   - Binary search has a time complexity of O(log n), making it significantly faster than linear search (O(n)), especially for large datasets. This efficiency becomes crucial in scenarios with extensive data.

2. **Sorted Data Requirement:**
   - Binary search requires the data to be sorted. However, if the data is already sorted or can be sorted efficiently, binary search becomes an excellent choice.

3. **Reduced Comparison Count:**
   - Binary search systematically halves the search space with each comparison, reducing the number of comparisons needed to find the target element. This is particularly advantageous for large datasets.

4. **Memory Efficiency:**
   - Binary search can be implemented in a memory-efficient manner as it typically requires only a constant amount of additional memory. This makes it suitable for scenarios with limited memory resources.

5. **Search in Ordered Collections:**
   - Binary search is ideal for ordered collections such as arrays or lists where the sorted nature of the data can be utilized to quickly pinpoint the target element.

6. **Real-Time Applications:**
   - Due to its logarithmic time complexity, binary search is suitable for real-time applications, especially when quick responses are needed, such as in certain types of search functionality.

7. **Algorithmic Understanding:**
   - Binary search is a fundamental algorithm and a classic example of a divide-and-conquer strategy. It is often taught in computer science courses and helps develop a deeper understanding of algorithmic principles.

8. **Use in Lower Level Programming:**
   - Binary search is commonly used in lower-level programming contexts or environments with limited resources, where simplicity and efficiency are crucial.

It's important to note that binary search is most effective when applied to sorted data. If the data is not sorted or sorting is too expensive, other search algorithms like linear search or hash-based search may be more appropriate. The choice of search algorithm depends on the specific characteristics and requirements of the data and the application.

## Real world use

A common real-world implementation of binary search is in search functionality for large datasets, such as a dictionary or a phonebook application. Here's an example scenario:

**Scenario: Dictionary Application**

Suppose a developer is working on a dictionary application where users can quickly look up the definitions of words. The application stores a large collection of words in alphabetical order.

**Implementation:**
1. **Data Structure:**
   - The dictionary is implemented as an array or a list of words, sorted alphabetically.

2. **Binary Search:**
   - When a user enters a word to search for its definition, the application employs binary search to quickly locate the word in the sorted collection.

3. **Efficiency:**
   - Binary search significantly reduces the number of comparisons needed to find the word compared to a linear search. This efficiency is crucial, especially when dealing with a large number of words.

4. **User Experience:**
   - Users experience faster response times when searching for words, enhancing the overall user experience of the dictionary application.

5. **Quick Navigation:**
   - Binary search allows users to quickly navigate through the alphabetically sorted list of words, making it convenient for them to find the word they are looking for.

Here's a simplified Python code snippet illustrating the binary search implementation for this scenario:

```python
def dictionary_search(dictionary, target_word):
    lo, hi = 0, len(dictionary) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if dictionary[mid] == target_word:
            return f"Definition of {target_word}: {get_definition(target_word)}"
        elif dictionary[mid] < target_word:
            lo = mid + 1
        else:
            hi = mid - 1

    return f"{target_word} not found in the dictionary."

def get_definition(word):
    # Placeholder function to retrieve the definition of a word
    # This could involve querying a database or other data source
    return "Lorem ipsum definition for " + word

# Example Usage
dictionary = ["apple", "banana", "cherry", "elephant", "zebra"]
target_word = "banana"
result = dictionary_search(dictionary, target_word)
print(result)
```

In this example, `dictionary_search` performs a binary search on the sorted dictionary to quickly locate the target word and return its definition. This kind of implementation enhances the efficiency of word lookup in a dictionary application or any other scenario with a similar requirement.