# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            count = 0
            if node.val >= max_so_far:
                count += 1
            new_max = max(node.val, max_so_far)
            
            left_count = dfs(node.left, new_max)
            right_count = dfs(node.right, new_max)
            
            return count + left_count + right_count
        
        return dfs(root, root.val)