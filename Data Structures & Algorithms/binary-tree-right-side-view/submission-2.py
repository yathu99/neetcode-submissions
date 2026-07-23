# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if (not root):
            return []
        nodes=[]
        def checkLevel(check,level):    
            if(len(nodes)<level):
                nodes.append(check.val if check else None)
            if(check.right):
                checkLevel(check.right,level+1)
            if(check.left):
                checkLevel(check.left,level+1)
        checkLevel(root,1)
        return nodes