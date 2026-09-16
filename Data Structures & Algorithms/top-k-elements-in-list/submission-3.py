class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        sort_num = sorted(count, key=count.get, reverse = True)
        res = []

        for i in range(k):
            res.append(sort_num[i])
        
        return res