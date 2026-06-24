class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nset = set()
        for n in nums:
            nset.add(n)
        
        if len(nums) > len(nset):
            return True
        else:
            return False