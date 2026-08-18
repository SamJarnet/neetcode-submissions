class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            seen = set()
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                if target in seen:
                    final = [nums[i], target, nums[j]]
                    if final not in lst:
                        lst.append(final)
                seen.add(nums[j])
        return lst