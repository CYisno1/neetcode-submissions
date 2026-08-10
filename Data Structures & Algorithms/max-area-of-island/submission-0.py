class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col): # 告訴我從 (row, col) 開始，這座島總共有多少格
        # dfs 的工作 =「走完整座島 + 回傳島的大小」
            if(
                row < 0 or row >= rows
                or col < 0 or col >= cols
                or grid[row][col] == 0
            ):
                return 0
            
            grid[row][col] = 0

            area = 1

            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)

            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(max_area, area)
        return max_area
            

