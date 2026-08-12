class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        time = 0
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        direction = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        while queue and fresh > 0:
            # 「這一分鐘一開始」有幾顆 rotten orange 要處理
            # 處理這一層所有 nodes: BFS level-order traversal
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in direction:
                    new_row = row + dr
                    new_col = col + dc

                    if (0 <= new_row < rows 
                        and 0 <= new_col < cols
                        and grid[new_row][new_col] == 1):
                        fresh -= 1
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))

            # 整個 BFS level 做完
            # 才代表過了一分鐘    
            time += 1
        
        # 如果還有 fresh orange
        # 代表有些 orange 永遠感染不到
        if fresh > 0:
            return -1

        return time

