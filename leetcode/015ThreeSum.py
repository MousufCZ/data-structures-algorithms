from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 2):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n -1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums [right]
                
                if current_sum < 0:
                    left += 1
                
                elif current_sum > 0:
                    right -= 1
                    
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    
                    while left > right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    while left < right and nums[right] == nums [right + 1]:
                        right -+ 1
                        
        return result
    

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    #nums = [-1, -1, -1, -1]
    solution = Solution()
    solutionOutput = solution.threeSum(nums)
    
    print(solutionOutput)


"""
Sorting and two pointer

"""