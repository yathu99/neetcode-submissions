class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l,r=0,0
        answers=[]
        def addBrack(string,l,r):
            if(r==n and l==n):
                return string
            if(r>l or r>n or l>n):
                return
            leftResult = addBrack(string+"(",l+1,r)
            rightResult = addBrack(string+")",l,r+1)
            if(leftResult):
                answers.append(leftResult)
            if(rightResult):
                answers.append(rightResult)
        addBrack("",0,0)
        return answers