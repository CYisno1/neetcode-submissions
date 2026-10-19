class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()

        for n in nums:
            nums_set.add(n)
        
        if len(nums_set) != len(nums):
            return True
        else:
            return False