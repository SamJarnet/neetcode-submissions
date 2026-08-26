class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False
        count = 0
        while not found:
            print(nums, count)
            if len(nums) == 1:
                if nums[0] == target:
                    found = True
                    return count
                else:
                    return -1
            mid = len(nums)//2
            if target < nums[mid]:
                nums = nums[:mid]
            else:
                nums = nums[mid:]
                count += mid


            
