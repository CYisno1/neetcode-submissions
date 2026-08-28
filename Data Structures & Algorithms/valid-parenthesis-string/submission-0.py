class Solution:
    def checkValidString(self, s: str) -> bool:
        # low  = 最少可能還剩幾個 unmatched '('
        # high = 最多可能還剩幾個 unmatched '('

        low = 0
        high = 0

        for char in s:
            if char == "(":
                low += 1
                high += 1
            
            elif char == ")":
                low = max(0, low - 1)
                high -= 1
            
            else: # "*"
                low = max(0, low - 1) # * -> )
                high += 1 # * -> (
            
            if high < 0:
                return False
            
        return low == 0