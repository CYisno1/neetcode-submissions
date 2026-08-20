class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        visited = [[False for c in range(len(grid[0]))] for r in range(len(grid))]
        dirction = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        res = 0
        cnt = 0

        def dfs(r, c):
            nonlocal cnt
            if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]) or \
                visited[r][c] == True or grid[r][c] == 0:
                return 0

            visited[r][c] = True
            cnt += 1

            for dr, dc in dirction:
                new_r = r + dr
                new_c = c + dc

                dfs(new_r, new_c)  

            return cnt    


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if visited[r][c] == False and grid[r][c] == 1:
                    cnt = 0
                    cnt = dfs(r, c)
                    res = max(res, cnt) 

        return res     