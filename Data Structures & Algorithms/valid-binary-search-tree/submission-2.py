# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, node: Optional[TreeNode]) -> bool:
        def dfs(root,left,right):
            if(not root):
                return True
            if not (left<root.val and root.val<right):
                return False
            return dfs(root.left,left,root.val) and dfs(root.right,root.val,right)
        return dfs(node,-99999999,99999999)
