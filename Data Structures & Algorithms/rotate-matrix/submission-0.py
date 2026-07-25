class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Rotate 90 deg: (r, c) -> (c, len(matrix) - r - 1)
        n = len(matrix)
        # Transpose: (r, c) -> (c, r)
        for r in range(n):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Flip column: (c, r) -> (c, len(matrix) - r - 1)
        for r in range(n):
            for c in range(n // 2):
                matrix[r][c], matrix[r][(len(matrix) - 1) - c] = matrix[r][(len(matrix) - 1) - c], matrix[r][c]
        