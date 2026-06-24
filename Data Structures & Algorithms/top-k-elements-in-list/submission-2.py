import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for n in nums:
            freq_dict[n] = 1 + freq_dict.get(n, 0)
        
        heap = []
        for n, f in freq_dict.items():
            heapq.heappush(heap, (f, n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in heap:
            result.append(i[1])
        return result

        