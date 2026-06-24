class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0

        for i in range(1, len(prices)):
            profit = prices[i] - buy
            res = max(res, profit)

            buy = min(buy, prices[i])
        
        return res
