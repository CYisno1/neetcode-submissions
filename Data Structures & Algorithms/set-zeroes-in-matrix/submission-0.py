class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        # 怎麼知道：matrix[0][1] == 0 
        # 是「column 1 要清零的 marker」，還是「第一 row 本身也應該全部清零」？
        # 所以你還需要額外記：
        first_row_zero = False
        first_col_zero = False

        for col in range(cols):
            if matrix[0][col] == 0:
                first_row_zero = True
        
        for row in range(rows):
            if matrix[row][0] == 0:
                first_col_zero = True
            
        # 用第一個 row 和第一個 column 當 marker
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    # 這個 row 之後全部要變 0
                    matrix[row][0] = 0
                    # 這個 col 之後全部要變 0
                    matrix[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                # 如果這個 row 的 marker 是 0，或這個 col 的 marker 是 0，這格就要變 0
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0  

        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0

        