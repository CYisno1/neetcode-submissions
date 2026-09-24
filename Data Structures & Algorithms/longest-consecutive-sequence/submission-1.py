class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            # num 是一段連續序列的起點
            if num - 1 not in nums_set:
                length = 1
                current = num

                while current + 1 in nums_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest

        

