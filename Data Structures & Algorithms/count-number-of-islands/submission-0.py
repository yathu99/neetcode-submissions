class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited= set()
        islands=0
        directions=[(0,-1),(-1,0),(1,0),(0,1)]
        def traverse(ind,visited):
            for direc in directions:
                newX=ind[0]+direc[0]
                newY=ind[1]+direc[1]
                if(newX>=0 and newX<len(grid) and newY>=0 and newY<len(grid[0]) and grid[newX][newY] == "1" and (newX,newY) not in visited):
                    visited.add((newX,newY))
                    traverse((newX,newY),visited)
            return 
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if(grid[x][y]=="1" and (x,y) not in visited):
                    traverse((x,y),visited)
                    islands+=1
        return islands

        
