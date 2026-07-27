class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # 直接把 nums 原地改成 heap

        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]