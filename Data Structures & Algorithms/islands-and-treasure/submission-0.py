class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
         # 1. 所有 treasure 都放進 queue
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # 2. BFS：BFS 開始之後，queue是「接下來還要往外擴散的格子」清單。
        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
            
                if (
                    new_row < 0 or new_row >= rows
                    or new_col < 0 or new_col >= cols
                ):
                    continue
                
                # 只可以走還沒處理過的 land
                if grid[new_row][new_col] == 2147483647:
                    grid[new_row][new_col] = grid[row][col] + 1
                    queue.append((new_row, new_col))
                
