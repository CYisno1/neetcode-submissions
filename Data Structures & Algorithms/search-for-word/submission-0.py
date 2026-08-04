class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, index):
            if index == len(word):
                return True
            
            # 防止走出棋盤
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] != word[index]
            ):
                return False
            
            # 做選擇：使用目前這一格
            temp = board[row][col]
            board[row][col] = "#"

            # 遞迴：選擇下一步要走哪個方向
            found = (
                dfs(row - 1, col, index + 1)
                or dfs(row + 1, col, index + 1)
                or dfs(row, col - 1, index + 1)
                or dfs(row, col + 1, index + 1)
            )

            # 撤銷選擇：把目前格子恢復
            board[row][col] = temp
            return found
        
        # 決定從哪一格開始
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        
        return False

        