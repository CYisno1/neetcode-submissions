# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 找到這一組的第 k 個節點
        def getKth(cur, k):
            while cur and k > 0:
                cur = cur.next
                k -= 1
            return cur

        dummy = ListNode(0, head)
        dummy.next = head

        # group_prev 永遠代表「目前這一組前面的那個節點」
        group_prev = dummy

        while True:
            kth = getKth(group_prev, k)

            # 找不到k代表剩下不足 k 個，結束
            if not kth:
                break
            
            group_next = kth.next

            # 反轉 group_prev.next 到 kth 這一段
            # prev 一開始設成 group_next
            # 這樣反轉完後，這組的尾巴會自動接回下一組
            prev = group_next
            cur = group_prev.next

            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            # 把前面接到反轉後的新頭
            # 反轉前的 group_prev.next 是這組的舊頭
            # 反轉後會變成這組的新尾巴，所以要先存起來
            old_group_head = group_prev.next

            # kth 是反轉後的新頭
            group_prev.next = kth

            # group_prev 移動到反轉後的新尾巴
            group_prev = old_group_head


        return dummy.next

