class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        result = [1] * n

        pref[0] = 1
        suff[n-1] = 1
        for i in range(1,n):
            pref[i] = nums[i - 1]*pref[i - 1]
        
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1]*suff[i + 1]
        
        for i in range(n):
            result[i] = pref[i]*suff[i]
        
        return result


        