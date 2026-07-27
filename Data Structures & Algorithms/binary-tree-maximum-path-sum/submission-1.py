# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            res = max(res, node.val + left + right)

            return node.val + max(left, right)
            # 這邊算的是目前 node 能提供多少給 parent
            # 傳給 parent 時不能分叉，所以只能選一邊
        
        dfs(root)
        return res