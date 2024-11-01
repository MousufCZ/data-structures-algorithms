from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1

        return print(maxProfit)

if __name__ == "__main__":
    testSolution = Solution()
    prices = [27, 51, 35, 38, 64, 24, 12, 49, 23, 45, 2]
    testSolution.maxProfit(prices)