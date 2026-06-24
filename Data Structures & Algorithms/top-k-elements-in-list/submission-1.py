class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}

        for n in nums:
            freq_dict[n] = 1 + freq_dict.get(n, 0)

        heap = []
        for n, f in freq_dict.items():
            heapq.heappush(heap, (f, n)) # f在n前面 這樣heap會用f來排序
            if len(heap) > k:
                heapq.heappop(heap) # heap裡面只留k個數
        
        res = []
        for i in heap:
            res.append(i[1]) # i[1] = n (num in nums)
        return res


            

        