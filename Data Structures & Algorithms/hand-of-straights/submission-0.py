class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        # 目前最小 = start
        # 必須找到：start, start + 1, start + 2, ..., start + groupSize - 1

        # duplicates 怎麼處理! ->> 需要想到Counter：我不只要知道某個 number 存不存在，還要知道它剩幾張
        count = Counter(hand)

        # min_heap → 現在最小的數字是誰？
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]
            # num 是「牌的數字本身」
            # 從目前最小的牌 start 開始，連續檢查 groupSize 張牌。
            for num in range(start, start + groupSize):
                # 這組需要 num，但已經沒有這張牌
                if count[num] == 0:
                    return False
                
                # 使用一張 num
                count[num] -= 1

                # 如果 num 被用完了
                if count[num] == 0:
                    # 它必須剛好也是目前最小的牌
                    if num != min_heap[0]:
                        return False

                    heapq.heappop(min_heap)
        
        return True

