class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        
        for i in range(1, len(prices)):
            profit = prices[i] - min(prices[0:i])
            if profit > max:
                max = profit

        return max