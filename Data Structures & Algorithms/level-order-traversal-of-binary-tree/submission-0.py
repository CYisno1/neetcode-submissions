# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def preorder(root, level):
            if not root:
                return
            
            if level == len(res):
                res.append([])
            
            res[level].append(root.val)

            preorder(root.left, level + 1)
            preorder(root.right, level + 1)
        
        preorder(root, 0)
        return res

            