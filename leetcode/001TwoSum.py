from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums [j] == target:
                    return print([i, j])

        return []

class Optimised:
    def twoSumOptimised(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            # dic = {index: value for index, value in i}
            dic.update
        return print(dic)

if __name__ == "__main__":
    nums = [1, 2, 7]
    testSolution = Solution()
    # testSolution.twoSum(nums, target=3)
    testSolution2 = Optimised()
    testSolution2.twoSumOptimised(nums, target=3)
    