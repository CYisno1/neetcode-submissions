# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return sametree(p.left, q.left) and \
            sametree(p.right, q.right)
        
        if not root:
            return False
        
        # Check whether the tree starting at the current node
        # is exactly the same as subRoot.
        if sametree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or \
        self.isSubtree(root.right, subRoot)
