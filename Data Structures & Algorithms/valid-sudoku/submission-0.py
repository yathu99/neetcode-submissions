class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for x in range(9)]
        columns=[set() for x in range(9)]
        block=[set() for x in range(9)]
        for x in range(9):
            for y in range(9):
                if(board[x][y]!='.'):
                    if(board[x][y] not in rows[x]):
                        rows[x].add(board[x][y])
                    else:
                        return False
                    if(board[x][y] not in columns[y]):
                        columns[y].add(board[x][y])
                    else:
                        return False
                    if(board[x][y] not in block[x//3*3+y//3]):
                        block[x//3*3+y//3].add(board[x][y])
                    else:
                        return False
        return True
