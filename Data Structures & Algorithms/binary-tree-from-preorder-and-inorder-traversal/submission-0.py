# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        # 當 preorder 已經沒有節點：代表這個位置沒有 subtree。

        root_val = preorder[0]
        root = TreeNode(root_val)

        # 在 inorder 找到 root 的位置
        mid = inorder.index(root_val)
        # mid 還代表左子樹有 mid 個節點!

        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

