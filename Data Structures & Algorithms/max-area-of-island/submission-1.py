class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if (
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
                    max_area = max(area, max_area)
        
        return max_area

            
            
            