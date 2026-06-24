class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                cur = n
                cur_len = 1

                while cur + 1 in nums_set:
                    cur += 1
                    cur_len += 1
                
                longest = max(longest, cur_len)
        
        return longest
                


        



