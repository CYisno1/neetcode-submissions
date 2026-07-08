class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canfinish(k):
            total_time = 0

            for pile in piles:
                total_time += (pile + k - 1) // k
            
            return total_time <= h
        
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            if canfinish(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
