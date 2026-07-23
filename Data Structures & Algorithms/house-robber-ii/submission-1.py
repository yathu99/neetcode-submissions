class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==3 or n==1):
            return max(nums)

        def robber(numst):
            n=len(numst)
            if(n<3):
                return max(numst)
            dp = [0] * (n)
            dp[n-1]=numst[-1]
            dp[n-2]=numst[-2]
            for x in range(n-3,-1,-1):
                if(x+3 < n):
                    dp[x]=numst[x]+max(dp[x+2],dp[x+3])
                else:
                    dp[x]=numst[x]+dp[x+2]
            return max(dp[0],dp[1])
        return max(nums[0],robber(nums[:-1]),robber(nums[1:]))
        