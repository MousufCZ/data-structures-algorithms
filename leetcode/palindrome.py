class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = 0
        xcopy = x

        if x < 0:
            return False

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return xcopy == reversed_num


numbers = list(range(10, 4000))
solver = Solution()
counter = 0

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        total = numbers[i] + numbers[j]
        if solver.isPalindrome(total):
            print(f"{numbers[i]} + {numbers[j]} = {total} --> Palindrome ✅")
    counter += 1


print(f"The total number of palindrome in the list is: {counter}")
