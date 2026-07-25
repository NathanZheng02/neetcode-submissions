class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefixMatrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            rowSum = 0
            for c in range(cols):
                rowSum += matrix[r][c]

                # Offset by 1 row and 1 col for consistency
                above = self.prefixMatrix[r][c + 1]
                self.prefixMatrix[r + 1][c + 1] = rowSum + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        diagRect = self.prefixMatrix[row1 - 1][col1 - 1]
        leftRect = self.prefixMatrix[row2][col1 - 1]
        topRect = self.prefixMatrix[row1 - 1][col2]
        currRect = self.prefixMatrix[row2][col2]

        # PIE
        return currRect - leftRect - topRect + diagRect    



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)