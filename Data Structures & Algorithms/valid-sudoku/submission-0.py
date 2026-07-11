from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create three dictionaries to store the values in rows, columns, and 3x3 squares
        cols = collections.defaultdict(set)  # Key: column index, Value: set of values in that column
        rows = collections.defaultdict(set)  # Key: row index, Value: set of values in that row
        squares = collections.defaultdict(set)  # Key: (row//3, col//3) representing the 3x3 square, Value: set of values in that square

        # Iterate over each cell in the Sudoku board
        for r in range(9):
            for c in range(9):
                # Skip cells with '.' (empty cells)
                if board[r][c] == ".":
                    continue

                # Check if the value is already present in the row, column, or 3x3 square
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    # If the value is a duplicate, the Sudoku is invalid
                    return False

                # Add the value to the corresponding row, column, and 3x3 square sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # If no duplicates are found, the Sudoku is valid
        return True
        
        
        