# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.high=0
        def depthBack(node):
            totalLength = 0
            lb=0
            rb=0
            if not node:
                return 0
            if(node.left):
                lb = depthBack(node.left)
            if(node.right):
                rb = depthBack(node.right)
            self.high=max(self.high,lb+rb)
            return 1+max(lb,rb)
        depthBack(root)
        return self.high
            
