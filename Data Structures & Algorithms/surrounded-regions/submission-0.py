class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col):
        # 只要 border 上看到 O，就從它開始 DFS
            if (row < 0 or row >= rows
                or col < 0 or col >= cols):
                return
            
            if board[row][col] != "O":
                return
            
            board[row][col] = "T" # Temporary safe

            # 繼續找上下左右相連的 O
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # 從上下左右的border找O
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)
            
        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)

        # 再掃一次整張 board
        for row in range(rows):
            for col in range(cols):    
                if board[row][col] == "O":
                    board[row][col] = "X"
                    
                elif board[row][col] == "T":
                    board[row][col] = "O"