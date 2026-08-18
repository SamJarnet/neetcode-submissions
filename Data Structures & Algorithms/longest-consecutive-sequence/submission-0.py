class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in range(0, len(nums)):
            if nums[i] -1 not in numSet:
                length = 0
                while (nums[i] + length in numSet):
                    length += 1
                if length > longest:
                    longest = length
        return(longest)