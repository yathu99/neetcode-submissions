class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if(n<3):
            return min(cost)
        dp = [0] * (n)
        dp[n-1]=cost[-1]
        dp[n-2]=cost[-2]
        for x in range(n-3,-1,-1):
            dp[x]=cost[x]+min(dp[x+1],dp[x+2])
        return min(dp[0],dp[1])