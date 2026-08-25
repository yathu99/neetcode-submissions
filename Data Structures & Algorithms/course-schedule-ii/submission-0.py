from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={k:[]for k in range(numCourses)}
        indegree={k:0 for k in range(numCourses)}
        for preq in prerequisites:
            adj[preq[1]].append(preq[0])
            indegree[preq[0]]+=1
        queue=deque()
        res=[]
        for indegree_check in indegree.keys():
            if indegree[indegree_check]==0:
                queue.append(indegree_check)
        while(queue):
            elem = queue.popleft()
            res.append(elem)
            for neighbor in adj[elem]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        if len(res)!=numCourses:
            return []
        return res
        
