# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root]) # deque() 接收的是一個可以逐個取出元素的集合，例如 list
        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # 代表目前的 node 就是這一層最後被處理的節點，也就是最右邊的節點。
                if i == level_size - 1:
                    res.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return res