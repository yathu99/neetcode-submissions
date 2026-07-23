# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if(not root):
            return 0
        maxval=root.val
        good=0
        def dfs(node,maxval):
            nonlocal good
            if(node):   
                if(maxval<=node.val):
                    good+=1
                    maxval=max(node.val,maxval)
                dfs(node.right,maxval)
                dfs(node.left,maxval)
        dfs(root,maxval)
        return good
                
