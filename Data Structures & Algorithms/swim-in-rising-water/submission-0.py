class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # min_heap 裡面放：
        # (走到這格至少需要的水位, row, col)
        min_heap = [(grid[0][0], 0, 0)]

        visited = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while min_heap:
            time, row, col = heapq.heappop(min_heap)

            if (row, col) in visited:
                continue
            
            visited.add((row, col))

            # 到達右下角
            if row == n - 1 and col == n - 1:
                return time
            
             # 往上下左右走
            for dr, dc in directions:
                new_r = row + dr
                new_c = col + dc

                # 超出 grid
                if (
                    new_r < 0 or new_r >= n
                    or new_c < 0 or new_c >= n
                ):
                    continue
                
                # 已經處理過就不用再走
                if (new_r, new_c) in visited:
                    continue
                
                # 到下一格至少需要多少水位？
                new_time = max(time, grid[new_r][new_c])
            
                heapq.heappush(min_heap, (new_time, new_r, new_c))