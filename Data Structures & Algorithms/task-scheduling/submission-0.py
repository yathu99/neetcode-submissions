class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        num_of_maxes=0
        maxcount=0
        hashes = dict.fromkeys(set(tasks),0)
        for x in range(len(tasks)):
            hashes[tasks[x]]+=1
            if(hashes[tasks[x]]==maxcount):
                num_of_maxes+=1
            if(hashes[tasks[x]]>maxcount):
                maxcount=hashes[tasks[x]]
                num_of_maxes=1
        return max(len(tasks),(maxcount-1)*(n+1)+num_of_maxes)

