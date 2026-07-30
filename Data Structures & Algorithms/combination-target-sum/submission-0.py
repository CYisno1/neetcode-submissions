class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, current, total):
        # i: 現在考慮current[i]
        # current: 目前選了哪些數字
        # total: 目前加總

            # base cases:
            if total == target:
                result.append(current.copy())
                return
            
            if total > target:
                return
            
            if i == len(nums):
            # 沒數字可以選了
                return
            
            # Choose nums[i]
            current.append(nums[i])
            dfs(i, current, total + nums[i]) # 不是i + 1因為i可以重複選
            current.pop()

            # Don't choose nums[i]
            dfs(i + 1, current, total)
        
        dfs(0, [], 0)
        return result
            
