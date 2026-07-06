class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2

            # Treat the matrix as a flattened sorted array.
            # Example: if cols = 4 and mid = 5,
            # row = 5 // 4 = 1, col = 5 % 4 = 1, so it maps to matrix[1][1].
            r = mid // cols
            c = mid % cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
