# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def getLength(head):
            length = 0

            while head:
                length += 1
                head = head.next
            
            return length
        
        if not head or not head.next:
            return
        
        n = getLength(head)
        if n % 2 == 0:
            index1 = n // 2 - 1
        else:
            index1 = n // 2
        
        # 1. 找到第一段的尾巴
        cur = head
        for _ in range(index1):
            cur = cur.next
        
        # 現在 cur 是第一段最後一個 node
        # second 是第二段的開頭
        second = cur.next

        # 斷開兩段
        cur.next = None

        # 2. 反轉第二段 linked list
        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 反轉完後，prev 是第二段新的 head
        second = prev

        # 3. 交錯 merge
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2


        





