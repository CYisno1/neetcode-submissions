class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort(key = lambda x: x[0])
        answer = [-1] * len(queries)

        min_heap = []
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        i = 0

        for query, index in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                size = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(min_heap, (size, intervals[i][1]))
                i += 1
            
            # min_heap 裝的是 (size, end)
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            # heap top 的 size 就是答案
            if min_heap:
                answer[index] = min_heap[0][0]
        
        return answer

