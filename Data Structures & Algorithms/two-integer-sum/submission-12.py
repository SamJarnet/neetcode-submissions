class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        for i in range(0, len(nums)):
            if target - nums[i] in previous:
                return ([previous[target - nums[i]], i])
            previous[nums[i]] = i
