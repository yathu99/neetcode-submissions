class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pas = [(position[x],(target-position[x])/speed[x],speed[x]) for x in range(len(position))]
        pas = sorted(pas,key=lambda x:x[0],reverse=True)
        fleet=1
        if len(position) > 1:
            anchor = pas[0][1]
            for index in range(1,len(pas)):
                if anchor < pas[index][1]:
                    fleet+=1
                    anchor = pas[index][1]
        return fleet