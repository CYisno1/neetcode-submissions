class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        # 第一輪：建立所有新 node
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # 第二輪：補上 next 和 random
        cur = head
        while cur:
            copy = old_to_new[cur]

            copy.next = old_to_new[cur.next] if cur.next else None
            copy.random = old_to_new[cur.random] if cur.random else None

            cur = cur.next

        return old_to_new[head] if head else None