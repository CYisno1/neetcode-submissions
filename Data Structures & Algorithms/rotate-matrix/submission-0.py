class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose + reverse row
        n = len(matrix)

        for row in range(n):
            for col in range(row + 1, n): # 只處理「對角線右上方」的格子!
                matrix[row][col],matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for row in matrix: # matrix 裡面的 row list
            row.reverse()
        
