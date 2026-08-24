class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp[i] = 前 i 個 characters 有幾種 decoding 方法
        dp = [0] * (n + 1)

        # empty prefix 當作一個合法的起始狀態
        dp[0] = 1

        for i in range(1, n + 1):
            # 檢查最後 1 位
            # 如果現在最後這個 digit 可以自己當一個字母，那前面有多少種解法，我現在就繼承多少種。
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            
            # 檢查最後 2 位
            # 如果最後兩個 digits 可以一起變成一個字母，那就把「去掉最後兩個 digits」的方法數也加進來。
            if i >= 2 and 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]
            
            