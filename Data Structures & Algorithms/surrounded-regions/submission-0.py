class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if (r not in range(rows) or c not in range(cols)
                or board[r][c] != "O"):
                return

            board[r][c] = "#"

            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. Capture all of the surrounded regions (O's -> #'s)
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and
                    (r == 0 or r == rows - 1 or
                     c == 0 or c == cols - 1)):
                    
                    capture(r, c)

        # 2. Capture the surrounded regions (Remaining O's -> X's)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Remark the unsurrounded regions (#'s -> O's)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
