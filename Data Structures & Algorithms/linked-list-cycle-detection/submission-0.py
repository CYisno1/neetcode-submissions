# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head # 一次走一步
        fast = head # 一次走兩步

        # 如果有迴圈 fast會追上slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
            
        
        return False


