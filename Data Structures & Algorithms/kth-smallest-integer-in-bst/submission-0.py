# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = None

        def inorder(node):
            nonlocal count, res
            if not node:
                return 0
            
            inorder(node.left) # 處理左邊

            count += 1 # 處理自己
            if count == k:
                res = node.val
                return

            inorder(node.right) # 處理右邊
        
        inorder(root)
        return res

