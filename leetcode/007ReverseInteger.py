class Solution:
    def reverse(self, x: int) -> int:
        
        result = 0

        MIN_INT = -(2**31)
        MAX_INT = 2**31 -1

        while x!= 0:
            if result < MIN_INT // 10 + 1 or result > MAX_INT // 10:
                return print("Null")
            
            digit = x % 10

            if x < 0 and digit > 0:
                digit -= 10

            result = result * 10 + digit

            x = (x - digit) // 10
        
        return result

if __name__ == "__main__":
    MIN_INT = -(2**31)
    MAX_INT = 2**31 -1
    print(MIN_INT)
    print(MAX_INT)



    callMethod = Solution()
    print(callMethod.reverse(x=345))