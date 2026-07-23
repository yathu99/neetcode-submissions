class Solution:

    def encode(self, strs: List[str]) -> str:
        if(strs==[]):
            return None
        return "`".join(strs)
    def decode(self, s: str) -> List[str]:
        if s==None:
            return []
        elif(len(s.split('`'))>0):
            return s.split('`')        