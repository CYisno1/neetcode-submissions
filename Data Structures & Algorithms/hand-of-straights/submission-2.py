class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        # 每個數字剩幾張
        freq = Counter(hand)

        # 從小到大處理
        nums = sorted(freq.keys())

        for x in nums:
            count = freq[x]

            if count > 0:
                # 這 count 張 x 全部都必須開一組
                for value in range(x, x + groupSize):
                    # 我要建立 count 組，
                    # 所以 value 至少也要有 count 張
                    if freq[value] < count:
                        return False
                    
                    # 同時用掉 count 張
                    freq[value] -= count
        
        return True
