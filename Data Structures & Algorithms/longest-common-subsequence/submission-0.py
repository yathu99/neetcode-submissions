class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        checkMap = [[0 for x in range(len(text2)+1)] for y in  range(len(text1)+1)]
        for a in range(len(text1)-1,-1,-1):
            for b in range(len(text2)-1,-1,-1):
                if text1[a]==text2[b]:
                    checkMap[a][b] = 1+checkMap[a+1][b+1]
                else:
                    checkMap[a][b] = max(checkMap[a+1][b],checkMap[a][b+1])
        return checkMap[0][0]