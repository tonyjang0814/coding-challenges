class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        seen = dict()
        for row in range(n):
            for col in range(n):
                if board[row][col] != ".":
                    _row = ("row",row,board[row][col])
                    _col = ("col",col,board[row][col])
                    _grid = ("grid",row//3,col//3,board[row][col])
                    if _row in seen or _col in seen or _grid in seen:
                        return False
                    else:
                        seen[_row] = 1
                        seen[_col] = 1
                        seen[_grid] = 1
        return True