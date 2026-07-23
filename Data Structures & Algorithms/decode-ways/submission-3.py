class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        invalid conditions
        1> digits selected are greater than 26. Ex - "2"+"9"
        2> leading zeroes. Ex - "0"+"7"
        '''
        dp=dict()
        def dfs(ind,val):
            if(int(val)>26 or int(val)==0 or int(val[0])==0 or val==""):
                dp[(val,ind)] = 0
                return 0
            if(ind==len(s)-1):
                dp[(val,ind)] =1
                return 1
            if(dp.get((val,ind))==None):
                left_check = dfs(ind+1,s[ind+1]) 
                right_check = dfs(ind+1,val+s[ind+1])
                dp[(val,ind)] = left_check + right_check
            return dp[(val,ind)]
        return dfs(0,s[0])
        