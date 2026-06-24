class Solution:
    def trap(self, height: List[int]) -> int:
        # the area at index i: min(height[l], height[r]) - height[i]
        n = len(height)
        pre = [0] * n
        suff = [0] * n

        # 從左往右掃，記錄每個位置左邊最高柱
        pre[0] = height[0]
        for i in range(1, n):
            pre[i] = max(pre[i - 1], height[i])
        
        # 從右往左掃，記錄每個位置右邊最高柱子
        suff[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = max(suff[i + 1], height[i])

        total = 0
        for i in range(n):
            water = min(pre[i], suff[i]) - height[i]
            total += water
        
        return total
            
             
        