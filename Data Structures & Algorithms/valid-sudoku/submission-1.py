class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in cols[r]
                    or board[r][c] in rows[c]
                    or board[r][c] in square[(r // 3, c // 3)]):
                    return False
                
                cols[r].add(board[r][c])
                rows[c].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
        
        return True