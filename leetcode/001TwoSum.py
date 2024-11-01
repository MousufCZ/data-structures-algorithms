from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] +nums [j] == target:
                    return print([i, j])

        return []

if __name__ == "__main__":
    testSolution = Solution()
    nums = [1, 2, 7]
    testSolution.twoSum(nums, target=3)