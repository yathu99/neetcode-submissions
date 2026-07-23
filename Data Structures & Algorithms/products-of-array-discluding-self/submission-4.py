class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct=1
        allZero=True
        zeroFound=0
        def checkZero(total,val):
            if(val==0):
                return total
            else:
                return 0
        for x in range(len(nums)):
            if(nums[x]==0):
                zeroFound+=1
            else:
                allZero=False
                totalProduct*=nums[x]
        if(allZero or zeroFound>1):
            return [ 0 for x in range(len(nums))]
        elif(zeroFound==1):
            return [checkZero(totalProduct,nums[z]) for z in range(len(nums))]
        else:
            return [int(totalProduct/nums[y]) for y in range(len(nums))]