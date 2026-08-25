class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # best = 一定要包含目前 nums[i] 的情況下，最大 subarray sum 是多少？
        # 所以走到每一個 nums[i] 時，你只有兩個選擇：
            # 重新開始：nums[i]
            # 接在前面的 best 後面：best + nums[i]
        best = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            best = max(nums[i], best + nums[i])

            res = max(res, best)
        
        return res
