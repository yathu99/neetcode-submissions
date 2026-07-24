class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[int(0) for y in range(n)] for x in range(m)]
        dp[m-1][n-1]=1
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if r==m-1 and c==n-1:
                    continue
                check_right = c+1
                check_down = r+1
                right_max= dp[r][check_right] if check_right<=n-1 else 0
                down_max= dp[check_down][c] if check_down<=m-1 else 0
                dp[r][c] = right_max + down_max    
        return dp[0][0]