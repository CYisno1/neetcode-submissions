class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        # subset 表示目前正在建立的 subset。
        # 它會在 recursion 過程中不斷被修改。

        # i 代表目前正在決定 nums[i]：要把它放進 subset，還是不放進 subset。
        def backtrack(i):
            if i == len(nums): # 當 i == len(nums)，代表 nums 裡每個數字都已經完成「選或不選」的決定。
                res.append(subset.copy())
                return
            
            # 選擇一：選了nums[i]
            subset.append(nums[i])

            backtrack(i + 1)
        
            # -----------------------------
            # Backtracking：回復原本狀態
            # -----------------------------

            # 上面的 recursion 已經完成所有『包含 nums[i]』的可能性。
            # 現在要探索「不包含 nums[i]」，所以先把剛才加入的 nums[i] 移除。
            subset.pop()

            # 選擇二：不選 nums[i]
            # 不需要修改 subset，直接前往下一個數字。
            backtrack(i + 1)
        
        # 從 nums[0] 開始進行選擇。
        backtrack(0)

        return res


