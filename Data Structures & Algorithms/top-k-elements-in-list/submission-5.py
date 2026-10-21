class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # {num : how many times}

        freq = [[] for _ in range(len(nums) + 1)]

        for num, times in count.items():
            freq[times].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res


        