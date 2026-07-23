class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if(n<3):
            return max(nums)
        dp = [0] * (n)
        dp[n-1]=nums[-1]
        dp[n-2]=nums[-2]
        for x in range(n-3,-1,-1):
            if(x+3 < n):
                dp[x]=nums[x]+max(dp[x+2],dp[x+3])
            else:
                dp[x]=nums[x]+dp[x+2]
        return max(dp[0],dp[1])