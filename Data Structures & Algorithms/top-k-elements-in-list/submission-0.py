class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_count = Counter(nums)

        # 取得前 k 高頻的 (Key, Value) 組合。例: [(1, 3), (2, 2)]
        frequent_pairs = num_count.most_common(k)

        return [num for num, freq in frequent_pairs]


            

        