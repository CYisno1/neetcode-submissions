class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            # 第一次取出的一定比較重，所以：y >= x

            if y != x:
                heapq.heappush(heap, -(y - x))
            
        if heap:
            return -heap[0] # 還剩一顆石頭
        else:
            return 0