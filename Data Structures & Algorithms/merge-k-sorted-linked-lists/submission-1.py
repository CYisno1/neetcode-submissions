# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        count = 0

        for node in lists:
            if node:
                heapq.heappush(min_heap, (node.val, count, node))
                count += 1
            
        dummy = ListNode()
        cur = dummy

        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            
            next_node = node.next

            cur.next = node
            cur = cur.next
            
            cur.next = None

            if next_node:
                heapq.heappush(min_heap, (next_node.val, count, next_node))
                count += 1
        
        return dummy.next
            

            