class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # ways[i] = 到第 i 階總共有幾種方法
        ways = [0] * (n + 1)

        # base case
        ways[1] = 1
        ways[2] = 2

        # DP
        for i in range(3, n + 1):
            # 到第 i 階：
            # 1. 可以從第 i-1 階走 1 步過來
            # 2. 可以從第 i-2 階走 2 步過來
            ways[i] = ways[i - 1] + ways[i - 2]
        
        return ways[n]

