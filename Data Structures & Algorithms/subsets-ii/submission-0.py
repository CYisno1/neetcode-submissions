class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, current):
            if i == len(nums): # 已經對每一個位置都做完「選或不選」的決定了
                res.append(current.copy())
                return
            
            # 選nums[i]
            current.append(nums[i])
            dfs(i + 1, current)
            current.pop()

            # 跳過重複的
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1, current)
        
        dfs(0, [])
        return res
            


