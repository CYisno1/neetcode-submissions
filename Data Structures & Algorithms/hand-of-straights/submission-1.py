class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]

            for num in range(start, start + groupSize):
                if count[num] == 0:
                    return False                
                
                count[num] -= 1

                if count[num] == 0:
                    if num != min_heap[0]:
                        return False
                
                    heapq.heappop(min_heap)
        
        return True
                
        