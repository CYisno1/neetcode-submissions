class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col): # 看到 O 就把它改成 T
            if (
                row < 0 or row >= rows
                or col < 0 or col >= cols
            ):
                return
            
            if board[row][col] != "O":
                return
            
            board[row][col] = "T"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        # 把有連到邊界的O改成T
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)
        
        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)

        # 掃整張圖
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"

