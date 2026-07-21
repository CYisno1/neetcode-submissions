# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 因為經過目前節點的最長路徑，是：左邊最深的 leaf -> 目前節點 -> 右邊最深的 leaf

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node):
            nonlocal diameter

            if not node:
                return 0
            
            left_h = height(node.left)
            right_h = height(node.right)

            diameter = max(diameter, left_h + right_h)

            return 1 + max(left_h, right_h)
        
        height(root)
        return diameter


        