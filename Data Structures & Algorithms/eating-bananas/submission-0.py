class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canfinish(k):
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k
            
            return total_hours <= h
        
        # both left and right are speed (try to find k)
        left = 1 # each pile needs at least need 1 hour to finish
        right = max(piles) # max speed like example 2

        while left <= right:
            mid = (left + right) // 2

            if canfinish(mid):
                right = mid - 1
                # mid works, but we want to find minimum k
            else:
                # mid is too slow, so we need a larger speed.
                left = mid + 1
        
        return left



        