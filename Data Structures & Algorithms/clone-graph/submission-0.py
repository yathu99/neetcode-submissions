"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited=dict()
        def copyNode(node):
            if  node in visited:
                return  visited[node]
            else:  
                children=[]
                newNode = Node(node.val)
                visited[node] = newNode
                for child in node.neighbors:
                    if child:
                        children.append(copyNode(child))
                newNode.neighbors=children
                return newNode
        return copyNode(node) if node else None
