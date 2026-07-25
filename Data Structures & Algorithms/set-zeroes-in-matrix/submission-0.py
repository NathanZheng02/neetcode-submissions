class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        # First Row edge case bc matrix[0][0] stores 0's for col
        firstRow = False

        # Marking all cases and storing it in the first row/col
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        firstRow = True
        
        # Check every case except first row/col
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # Check first col
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        # Check first row
        if firstRow:
            for c in range(cols):
                matrix[0][c] = 0
        