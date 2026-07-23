class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        occ=dict()
        if(len(s1)>len(s2)):
            return False
        for x in s1:
            if x not in occ:
                occ[x]=1
            else:
                occ[x]+=1
        l,r=0,len(s1)
        while(l<r and r<=len(s2)):
            tempdict=occ.copy()
            for j in range(l,r):
                if(s2[j] in tempdict and tempdict[s2[j]]>0):
                    tempdict[s2[j]]-=1
                    if(tempdict[s2[j]]==0):
                        tempdict.pop(s2[j])
                    if(len(tempdict)==0):
                        return True
                else:
                    l+=1
                    r+=1
                    break
        return False