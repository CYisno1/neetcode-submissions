class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # h = min(h[in1], h[in2])
        # w = in2 - in1
        res = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            area = min(heights[right], heights[left]) * (right - left)
            res = max(res, area)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return res



