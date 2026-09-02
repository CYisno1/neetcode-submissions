class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            else:
                digits[i] = 0
        
        # 它只有在「整個 loop 都沒有 return」的情況下才會執行
        # 例如：digits = [9,9,9] → 最前面補一個 1
        return [1] + digits


