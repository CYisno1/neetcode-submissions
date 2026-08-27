class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            best = max(nums[i], best + nums[i])

            res = max(res, best)
        
        return res