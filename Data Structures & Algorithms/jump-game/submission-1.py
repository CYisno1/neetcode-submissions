class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
                
            farthest = max(farthest, i + nums[i])
            # My previous farthest reachable index was farthest. From the current index, I can reach i + nums[i].
            # I'll keep whichever one is farther.
            
            
        return True   