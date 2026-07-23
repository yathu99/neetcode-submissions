# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (not root):
            return []
        nodes=[]
        def checkLevel(check,level):    
            if(check):
                if(level >= len(nodes)):
                    nodes.insert(level,[])
                nodes[level].append(check.val)
                if(check.left):
                    checkLevel(check.left,level+1)
                if(check.right):
                    checkLevel(check.right,level+1)
        checkLevel(root,0)
        return nodes