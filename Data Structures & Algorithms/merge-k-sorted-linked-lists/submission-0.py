import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        count = 0

        # 1. 一開始只把每條 list 的 head 放進 heap
        for node in lists:
            if node:
                heapq.heappush(min_heap, (node.val, count, node))
                count += 1

        # 2. 建立答案 linked list
        dummy = ListNode(0)
        cur = dummy

        # 3. heap 不空，就一直拿出目前最小的 node
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            # _: 代表「這個值我不想用」

            # 先記住 node 原本的下一個節點
            next_node = node.next

            # 把目前最小的 node 接到答案後面
            cur.next = node
            cur = cur.next

            # 斷開，避免舊 linked list 關係干擾
            cur.next = None

            # 如果這個 node 後面還有節點，把下一個節點放進 heap
            if next_node:
                heapq.heappush(min_heap, (next_node.val, count, next_node))
                count += 1
            

        return dummy.next