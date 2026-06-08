class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.row_valid(board) and
            self.column_valid(board) and
            self.mini_grid_valid(board)
        )
    def mini_grid_valid(self, board):
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                grid = [
                    board[r][c]
                    for r in range(box_row, box_row + 3)
                    for c in range(box_col, box_col + 3)
                ]
                if not self.values_diff(grid):
                    return False
        return True

    def row_valid(self, board):
        return all([self.values_diff(row) for row in board])
    
    def column_valid(self, board):
        transposed = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
        return all([self.values_diff(col) for col in transposed])

    def values_diff(self, lists):
        value = set()
        for val in lists:
            if val == ".":
                continue
            if val in value:
                return False
            else:
                value.add(val)
        return True