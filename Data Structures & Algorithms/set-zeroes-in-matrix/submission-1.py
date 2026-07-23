class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        row_check=[False] * rows
        col_check=[False] * cols
        for indeX,x in enumerate(matrix):
            for indeY,y in enumerate(x):
                if(matrix[indeX][indeY]==0):
                    row_check[indeX]=True
                    col_check[indeY]=True
        for nx,dx in enumerate(row_check):
            if(dx):
                for y in range(cols):
                    matrix[nx][y]=0
        for ny,dy in enumerate(col_check):
            if(dy):
                for y in range(rows):
                    matrix[y][ny]=0
        

        