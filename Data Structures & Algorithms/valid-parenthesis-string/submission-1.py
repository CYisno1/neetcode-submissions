class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for char in s:
            if char == "(":
                low += 1
                high += 1
            
            elif char == ")":
                low = max(0, low - 1)
                high -= 1
            
            else:
                low = max(0, low - 1)
                high += 1
            
            if high < 0:
                return False
            # 即使把所有可能的 * 都盡量當成 (，還是沒有足夠的左括號配現在的 )
        
        if low > 0:
            return False
        
        return True
