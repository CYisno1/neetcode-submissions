# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def getkth(cur, k):
            while cur and k > 0:
                cur = cur.next
                k -= 1
            return cur

        dummy = ListNode(0, head)
        
        group_prev = dummy
        while True:
            kth = getkth(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            
            prev = group_next
            cur = group_prev.next

            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            old_group_head = group_prev.next
            group_prev.next = kth
            group_prev = old_group_head
        
        return dummy.next
            
            

        
        