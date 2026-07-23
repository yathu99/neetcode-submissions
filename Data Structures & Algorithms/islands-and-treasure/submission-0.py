class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        INF = 2147483647
        queue=[]
        steps=[(0,1),(0,-1),(1,0),(-1,0)]
        maxTime=0
        for x in range(m):
            for y in range(n):
                if grid[x][y]==0:
                    queue.append(((x,y),0))
        while(len(queue) > 0):
            newNode = queue.pop(0)
            print("Checking ",newNode)
            [x,y] = newNode[0]
            if grid[x][y] == INF or grid[x][y]== 0:
                grid[x][y]=min(grid[x][y],newNode[1])
                for step in steps:
                    dx = x + step[0]
                    dy = y + step[1]
                    if dx >= 0 and dx < m and dy >= 0 and dy < n and (dx,dy) and grid[dx][dy]>0:
                        queue.append(((dx,dy),newNode[1]+1))