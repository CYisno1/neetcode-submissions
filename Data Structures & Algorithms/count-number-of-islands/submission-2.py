class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0

        visited = [[False for col in range(len(grid[0]))] for row in range(len(grid))]

        def dfs(r, c):

            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or \
                visited[r][c] == True or grid[r][c] == "0":
                return

            visited[r][c] = True

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if visited[r][c] == False and grid[r][c] == "1":
                    dfs(r, c)
                    res += 1

        return res

            