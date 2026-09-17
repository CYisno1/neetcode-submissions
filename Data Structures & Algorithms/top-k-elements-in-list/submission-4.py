class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 建立 bucket，index 代表「出現幾次」
        # 最後從後面往前找 拿到 k 個就 return

        count = Counter(nums)

        freq = [[] for _ in range(len(nums) + 1)]
        # 一個數字最多可能出現 len(nums) 次 因此 bucket 要有 index：共 n + 1 個

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res