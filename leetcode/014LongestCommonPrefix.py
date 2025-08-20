def longestCommonPrefix(arr):
    # Sort the list of strings
    arr.sort()
    print("After sorting:", arr)

    # Get the first and last strings after sorting
    first = arr[0]
    last = arr[-1]
    print("First:", first)
    print("Last:", last)

    # Find the minimum length between the two
    minLength = min(len(first), len(last))
    print("Minimum length to compare:", minLength)

    i = 0
    # Compare characters one by one
    while i < minLength and first[i] == last[i]:
        print(f"Comparing first[{i}]={first[i]} with last[{i}]={last[i]} → Match!")
        i += 1

    # Return the common prefix
    return first[:i]


if __name__ == "__main__":
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
    print("Longest Common Prefix:", longestCommonPrefix(arr))
