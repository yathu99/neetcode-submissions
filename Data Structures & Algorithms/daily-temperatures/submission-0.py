class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        if(len(temps)==1):
            return temps
        l,r=0,1
        ans=[]
        while(l<r and l<len(temps)):
            while(r<len(temps)):
                if(temps[r]>temps[l]):
                    ans.append(r-l)
                    break
                else:
                    r+=1
            if(r>=len(temps)):
                ans.append(0)
            l+=1
            r=l+1
        return ans