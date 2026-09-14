class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0

        for num in nums:
            result ^= num

        return result
    
    # 把數字轉成 binary 後，每一個 bit 分別 XOR
    # XOR 是「兩個 bit 不一樣才是 1」
    # XOR 還有一個重要特性：順序不重要