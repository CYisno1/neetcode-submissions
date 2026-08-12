class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(row, col, visited):
            # 來到這個 cell，代表它可以流到目前正在搜尋的 ocean
            visited.add((row, col))

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (new_row,new_col) in visited:
                    continue
                
                if (new_row < 0 or new_row >= rows
                    or new_col < 0 or new_col >= cols):
                    continue
                
                if heights[new_row][new_col] < heights[row][col]:
                    continue
                
                # neighbor >= current
                # 代表 neighbor 的水原本可以流到 current
                # 所以繼續往 neighbor DFS
                dfs(new_row, new_col, visited)
        
        # Pacific 接觸 top row
        for col in range(cols):
            dfs(0, col, pacific)

        # Pacific 接觸 left column
        for row in range(rows):
            dfs(row, 0, pacific)
        
        # Atlantic
        for col in range(cols):
            dfs(rows - 1, col, atlantic)

        for row in range(rows):
            dfs(row, cols - 1, atlantic)
        
        # 找同時存在於兩個 set 的 cell
        res = []

        for row in range(rows):
            for col in range(cols):
                # 同時可以流到 Pacific + Atlantic
                if (
                    (row, col) in pacific
                    and (row, col) in atlantic
                ):
                    res.append([row, col])

        return res
                