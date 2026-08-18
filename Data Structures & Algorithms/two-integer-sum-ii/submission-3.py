class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = 0
        num = None
        num_set = set(numbers)
        started = False
        for i in range(0, len(numbers)):
            if target - numbers[i] in num_set and started == False:
                first = i
                num = target - numbers[i]
                started = True
            if numbers[i] == num:
                second = i
        return([first+1, second+1])
            