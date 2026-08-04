class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []       # 存所有完整排列
        current = []   # 目前正在建立的排列
        used = [False] * len(nums)     # 記錄哪些數字已經使用過 

        def dfs(): # 不是「沒有狀態」，而是狀態存放在外層的 current 和 used 裡
            if len(current) == len(nums):
                res.append(current.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                # 遇到已經用過的數字就跳過

                # 選nums[i]
                used[i] = True
                current.append(nums[i])

                # backtracking
                dfs()

                # 撤銷選擇
                current.pop()
                used[i] = False
            
        dfs()
        return res


