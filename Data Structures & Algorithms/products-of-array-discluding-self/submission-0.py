
from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num = 1
        arr = []

        def prod(nums):
            num = 1
            for i in range(0, len(nums)):
                num *= nums[i]
            return num

        num = prod(nums)

        for i in range(0, len(nums)):
            if nums[i] != 0:
                arr.append(int(num / nums[i]))
            else:
                temp = nums[:i] + nums[i+1:]
                arr.append(prod(temp))
        return arr