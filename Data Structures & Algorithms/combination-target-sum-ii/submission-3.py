class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # 1, 2, 2, 4, 5, 6, 9

        res = []
        current = []

        def dfs(start, total):

            if total == target:
                res.append(current.copy())
                return
            
            for i in range(start, len(candidates)):
                if total + candidates[i]> target:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                current.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                current.pop()

        
        dfs(0, 0)
        return res



