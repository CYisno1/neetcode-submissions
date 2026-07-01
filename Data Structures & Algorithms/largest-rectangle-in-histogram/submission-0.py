class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 對每個 bar，找它左邊第一個更矮的 bar，和右邊第一個更矮的 bar。

        stack = []  # 存 index，讓 heights[index] 保持遞增
        res = 0

        for i in range(len(heights) + 1):
            current_h = heights[i] if i < len(heights) else 0

            while stack and current_h < heights[stack[-1]]:
                height = heights[stack.pop()]

                left_boundary = stack[-1] if stack else -1

                width = i - left_boundary - 1

                res = max(res, height * width)
            
            stack.append(i)
        
        return res
