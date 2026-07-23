class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited= set()
        maxIsland=0
        directions=[(0,-1),(-1,0),(1,0),(0,1)]
        def traverse(ind,visited):
            newIsland=1
            for direc in directions:
                newX=ind[0]+direc[0]
                newY=ind[1]+direc[1]
                if(newX>=0 and newX<len(grid) and newY>=0 and newY<len(grid[0]) and grid[newX][newY] == 1 and (newX,newY) not in visited):
                    visited.add((newX,newY))
                    newIsland+=traverse((newX,newY),visited)
            return newIsland
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if(grid[x][y]==1 and (x,y) not in visited):
                    visited.add((x,y))
                    thisIsland=traverse((x,y),visited)
                    maxIsland= max(maxIsland,thisIsland)
        return maxIsland
