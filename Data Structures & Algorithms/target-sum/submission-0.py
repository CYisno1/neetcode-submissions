from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[sum] = 用到目前這些數字時，
        # 有幾種方法可以得到這個 sum
        #
        # 一開始還沒用任何數字：
        # sum = 0 有 1 種方法
        # 就是「什麼都還沒做」
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:

            # 這一輪要建立新的 dp
            # 因為我們要根據「上一輪的 dp」
            # 來算加上現在這個 num 之後的新狀態
            new_dp = defaultdict(int)

            for current_sum, ways in dp.items():
                # 選擇 1：現在這個 num 放 +
                new_dp[current_sum + num] += ways

                # 選擇 2：現在這個 num 放 -
                new_dp[current_sum - num] += ways
            
            # 現在這個 num 處理完了
            # 把新的狀態變成下一輪的 dp
            dp = new_dp
        
        # dp[target] 就是最後得到 target 的方法數
        # 如果 target 根本不存在，
        # defaultdict(int) 會自動回傳 0
        return dp[target]

        