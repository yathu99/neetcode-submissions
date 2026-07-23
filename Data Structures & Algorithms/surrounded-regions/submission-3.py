class Solution:
    def solve(self, board: List[List[str]]) -> None:
        borders=set()
        steps=[(0,1),(1,0),(-1,0),(0,-1)]
        for k in range(len(board)):
            if board[k][0]=="O":
                borders.add((k,0))
            if board[k][len(board[0])-1]=="O" and len(board[0])>1:
                borders.add((k,len(board[0])-1))
        for l in range(len(board[0])):
            if board[0][l]=="O":
                borders.add((0,l))
            if len(board[0])>1 and board[len(board)-1][l]=="O":
                borders.add((len(board)-1,l))
        visited = set()
        curQueue = [z for z in borders]
        while len(curQueue)>0:
            node = curQueue.pop(0)
            x=node[0]
            y=node[1]
            if board[x][y]=="O" or board[x][y]=="1" and (x,y) not in visited:
                for z in steps:
                    dx = x+z[0]
                    dy = y+z[1]
                    if (dx,dy) not in visited and 0<dx<len(board)-1 and 0<dy<len(board[0])-1 and board[dx][dy]=="O":
                        print("adding",[dx,dy])
                        board[dx][dy]="1"
                        curQueue.append([dx,dy])
            visited.add((x,y))
        for a in range(1,len(board)-1):
            for b in range(1,len(board[0])-1):
                if board[a][b]=="1":
                    board[a][b]="O"
                elif board[a][b]=="O":
                    board[a][b]="X"