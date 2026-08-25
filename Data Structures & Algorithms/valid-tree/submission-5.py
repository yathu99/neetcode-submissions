from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited=[False for x in range(n)]
        adj={k:[] for k in range(n)}
        q = deque()
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        q.append((0,-1))
        while(q):
            elem, parent = q.popleft()
            for neighbor in adj[elem]:
                if neighbor == parent:
                    continue
                if visited[neighbor]:
                    return False
                q.append((neighbor,elem))
            visited[elem]=True
        return all(visited)