class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 1. 把 cells 按 elevation 收集起來
        cells = []

        for row in range(n):
            for col in range(n):
                cells.append((grid[row][col], row, col))
        
        cells.sort()
    
        # 2. Union Find
        parent = list(range(n * n))

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
        
        # 3. Track active cells
        active = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

         # 4. 水位由低到高 activate cells
        for elevation, row, col in cells:
            active.add((row, col))

            node1 = row * n + col

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                node2 = new_row * n + new_col

                if (
                    new_row < 0 or new_row >= n
                    or new_col < 0 or new_col >= n
                ):
                    continue

                if (new_row, new_col) not in active:
                    continue
                
                node2 = new_row * n + new_col
                union(node1, node2)

            # start 和 end 已經 connected -> 現在是不是已經在同一個 component
            if find(0) == find(n * n - 1):
                return elevation



