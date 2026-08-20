class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(r, c):
            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or grid[r][c] == 0
                or (r, c) in visited
            ):
                return 0
            
            visited.add((r, c))
            area = 1

            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(area, max_area)

        return max_area