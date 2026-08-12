class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(0, len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        sort = {}
        for key in sorted(count, key=count.get):
            sort[key] = count[key]
        return(list(sort)[-k:])
