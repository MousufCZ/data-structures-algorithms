class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        
        currentRow = 0
        direction = -1

        for char in s:
            rows[currentRow].append(char)

            if currentRow == 0 or currentRow == numRows -1:
                direction =- direction

            currentRow += direction

        return print(''.join(''.join(row) for row in rows))
    
if __name__ == '__main__':
     s = "PAYPALISHIRING"
     callMethod = Solution()
     callMethod.convert(s, numRows=3)