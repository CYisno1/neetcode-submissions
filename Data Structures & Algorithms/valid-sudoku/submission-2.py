from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if (num in row[r]
                    or num in col[c]
                    or num in square[(r // 3, c // 3)]):
                    return False

                row[r].add(num)
                col[c].add(num)
                square[(r // 3, c // 3)].add(num)

        return True