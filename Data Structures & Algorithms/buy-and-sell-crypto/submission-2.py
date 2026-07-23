class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        profit=0
        while(l<r and r<len(prices)):
            if(prices[r]>=prices[l]):
                profit=max(profit,prices[r]-prices[l])
            elif(prices[r]<prices[l]):
                l=r
            r+=1 
        return profit
