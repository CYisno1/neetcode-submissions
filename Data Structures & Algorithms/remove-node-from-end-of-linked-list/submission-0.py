# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 建立 dummy node: 一個假的開頭，放在原本 head 前面        
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # 先讓 fast 往前走 n + 1 步
        # 這樣 fast 和 slow 中間會隔著 n 個 node
        # 之後兩個一起走，slow 才會停在要刪的前一個
        for _ in range(n + 1):
            fast = fast.next
        
        # fast 和 slow 一起往後走
        # 當 fast 走到 None，slow 就會在要刪除 node 的前一個位置
        while fast:
            fast = fast.next
            slow = slow.next

        # slow.next 是要刪的 node
        # slow.next.next 是刪掉之後要接上的 node
        slow.next = slow.next.next

        return dummy.next





        