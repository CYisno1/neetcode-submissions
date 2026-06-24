class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0

        for i in range(1, len(prices)):
            profit = prices[i] - buy
            res = max(res, profit)

            # buy 不是固定的，它會隨著你往右走一直更新成「目前看過的最低價」
            buy = min(prices[i], buy)

        return res



        