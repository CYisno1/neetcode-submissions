class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            if n == 1:
                return True

            seen.add(n)

            total = 0
            while n:
                digit = n % 10 # 最後一位
                total += digit * digit
                n = n // 10 # 從個位數處理到十位數 依序往左處理
            
            n = total
        
        # 如果某一天：n in seen 代表 cycle 出現，while 自動停止，所以最後：
        return False
        