class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_set = set([f"{i}" for i in range(1, 10)])
        
        
        for i in range(9):
            row_table = set()
            col_table = set()
            for j in range(9):
                # check rows
                if board[i][j] in num_set:
                    if board[i][j] in row_table:
                        return False
                    else:
                        row_table.add(board[i][j])
                # check columns
                if board[j][i] in num_set:
                    if board[j][i] in col_table:
                        return False
                    else:
                        col_table.add(board[j][i]) 

        vertex = [(i, j) for i in [0, 3, 6] for j in [0, 3, 6]]
        # check blocks
        for i, j in vertex:
            block_table = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if board[row][col] in num_set:
                        if board[row][col] in block_table:
                            return False
                        else:
                            block_table.add(board[row][col])

        return True