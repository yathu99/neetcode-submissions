class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)     #COLS
        n=len(board[0])  #ROWS
        direc=[(-1,0),(1,0),(0,-1),(0,1)]
        res=False
        def dfs(curr,letter):
            if board[curr[0]][curr[1]] == word[letter]:
                visited.add(curr)
                if letter == len(word)-1:
                    return True
                k1 = False
                for dir in direc:
                    d1 = dir[0]+curr[0]
                    d2 = dir[1]+curr[1]
                    if d1>=0 and d1<m and d2>=0 and d2<n and (d1,d2) not in visited:
                        ans = dfs((d1,d2),letter+1)
                        k1 = k1 or ans
                        if not ans and (d1,d2) in visited:
                            visited.remove((d1,d2))
                return k1
            return False
        for x in range(m):
            for y in range(n):
                visited=set()
                res = res or dfs((x,y),0)
                visited.clear()
                if res:
                    return res
        return False