class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        if nums[0] > nums[-1]:
            for i in reversed(nums):
                if i > minimum:
                    return minimum
                if i < minimum:
                    minimum = i
        else:
            for i in nums:
                if i < minimum:
                    return i
        return minimum