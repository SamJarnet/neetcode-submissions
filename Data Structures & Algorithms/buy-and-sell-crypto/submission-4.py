class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        seen = prices[0]
        max = 0
        for i in range(0, len(prices)):
            profit = prices[i] - seen
            if profit > max:
                max = profit
            if prices[i] < seen:
                seen = prices[i]
        return max