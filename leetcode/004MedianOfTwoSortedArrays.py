from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two sorted arrays
        merged = sorted(nums1 + nums2)
        length = len(merged)
        
        # Check if the total length is even or odd
        if length % 2 == 0:
            # If even, return the average of the two middle elements
            return print((merged[length // 2 - 1] + merged[length // 2]) / 2)
        else:
            # If odd, return the middle element
            return print(merged[length // 2])


if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2]
    callMethod = Solution()
    callMethod.findMedianSortedArrays(nums1, nums2)
