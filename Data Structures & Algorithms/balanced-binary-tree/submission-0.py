# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node): # 算的是以 node 為根的這棵子樹有多高
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)

            if left == -1:
                return -1
            
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)

        return height(root) != -1

        