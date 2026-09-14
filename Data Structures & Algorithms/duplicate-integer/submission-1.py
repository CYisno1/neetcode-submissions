class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_2 = set()

        for num in nums:
            nums_2.add(num)
        
        return len(nums_2) != len(nums)