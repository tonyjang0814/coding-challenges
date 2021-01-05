class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        board_cpy = list()
        #   copy original board to pass as an argument in function.
        for i in range(row):
            row_lst = list()
            for j in range(col):
                row_lst.append(board[i][j])
            board_cpy.append(row_lst)
        
        for i in range(row):
            for j in range(col):
                counts = self.liveCounts(board_cpy,i,j,row,col)
                if board_cpy[i][j] == 1: #if looking at live element.
                    if counts < 2: # under-poplulation
                        board[i][j] = 0
                    elif counts == 2 or counts == 3:
                        board[i][j] = 1
                    else: # over-population
                        board[i][j] = 0
                else: # if looking at dead element.
                    if counts == 3:       
                        board[i][j] = 1
        print(board)
    
    def liveCounts(self,board,row_idx,col_idx,row,col):
            count = 0
            for i,j in [(row_idx-1,col_idx-1),(row_idx-1,col_idx),(row_idx-1,col_idx+1),(row_idx,col_idx-1),(row_idx,col_idx+1),(row_idx+1,col_idx-1),(row_idx+1,col_idx),(row_idx+1,col_idx+1)]:
                if i >= 0 and i < row and j >= 0 and j < col:
                    if board[i][j] == 1:
                        count += 1
            return count