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
        
        cur = head
        for _ in range(index1):
            cur = cur.next
        
        second = cur.next

        cur.next = None

        curr = second
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        second = prev

        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2
        
        

            
            

