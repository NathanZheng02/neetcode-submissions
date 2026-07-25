from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        What is going on?
        - Creating 3 hashmaps that maps the key to a set value (1 - 9)
        - This allows us to check if there are unique 1 to 9 values in the specific row, column, or 3x3 box
        - For 3x3 box, we have to create a tuple key for each of the 9 boxes in Sodoku
        '''
        cols = defaultdict(set)
        rows = defaultdict(set)
        three_by_three = defaultdict(set) # Key = (r / 3, c / 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in three_by_three[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                three_by_three[(r // 3, c // 3)].add(board[r][c])
        return True
                