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

    """
    nums = [2, 3, 6, 7]
    target = 7
    
    dfs(0, [], 0)
    │
    ├── 選 2
    │   dfs(0, [2], 2)
    │   │
    │   ├── 選 2
    │   │   dfs(0, [2,2], 4)
    │   │   │
    │   │   ├── 選 2
    │   │   │   dfs(0, [2,2,2], 6)
    │   │   │   └── 繼續選 2 → 8，超過
    │   │   │
    │   │   └── 不選 2，改看 3
    │   │       └── 選 3 → [2,2,3] = 7 ✅
    │   │
    │   └── 不選 2，改看 3
    │       dfs(1, [2], 2)
    │       └── 找不到答案
    │
    └── 不選 2
        dfs(1, [], 0)
        │
        ├── 嘗試 3 → 找不到答案
        ├── 嘗試 6 → 找不到答案
        └── 嘗試 7
            └── [7] = 7 ✅
    """    
