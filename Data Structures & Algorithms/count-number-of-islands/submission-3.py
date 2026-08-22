class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        parent = list(range(rows * cols))

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
        
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(a, b):
            roota = find(a)
            rootb = find(b)

            if roota == rootb:
                return False
            
            parent[rootb] = roota
            return True
        
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0":
                    continue
                
                node1 = row * cols + col

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if(
                        new_row < 0 or new_row >= rows
                        or new_col < 0 or new_col >= cols
                    ):
                        continue
                    
                    # neighbor 也是 land → 嘗試合併
                    if grid[new_row][new_col] =="1":
                        node2 = new_row * cols + new_col
                    
                        if union(node1, node2):
                            count -= 1
        
        return count