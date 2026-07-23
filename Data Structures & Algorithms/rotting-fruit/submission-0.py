class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue=[]
        steps=[(0,1),(0,-1),(1,0),(-1,0)]
        maxTime=0
        for x in range(m):
            for y in range(n):
                if grid[x][y]==2:
                    queue.append(((x,y),0))
        while(len(queue) > 0):
            newNode = queue.pop(0)
            [x,y] = newNode[0]
            if grid[x][y] <= 2 and grid[x][y]>0:
                maxTime = max(maxTime,newNode[1])
                grid[x][y]=0
                for step in steps:
                    dx = x + step[0]
                    dy = y + step[1]
                    if dx >= 0 and dx < m and dy >= 0 and dy < n and (dx,dy) and grid[dx][dy]==1:
                        queue.append(((dx,dy),newNode[1]+1))
        for x in range(m):
            for y in range(n):
                if grid[x][y]==1:
                    return -1
        return maxTime