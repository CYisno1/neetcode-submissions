class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/ x
            n = -n
        
        res = 1
        while n > 0:
            if n % 2 == 1: # n 是奇數
                res = res * x
            
            x = x * x
            # 每次把 exponent 砍一半
            n = n // 2
        
        return res
    
    # n 偶數：不用先拿一個 x 出來，直接把 x 平方、n 除 2。
    # x⁶ = (x²)³
    # n 奇數：多出一個 x，所以先 res *= x，再做同樣的平方和除 2。
    # x⁵ = x × (x²)²