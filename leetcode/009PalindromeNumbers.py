class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            x = str(x)
            if x == x[::-1]:
                return True
            else:
                return False

if __name__ == "__main__":
    nums = [121]
    testSolution1 = Solution()
    testSolution1.isPalindrome(121)