class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def dfs(start, current, total):
            if total == target:
                res.append(current.copy())
                return
            
            for i in range(start, len(candidates)):
                num = candidates[i]
            
                if total + num > target:
                    break
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                current.append(num)
                dfs(i + 1, current, total + num)
                current.pop()
            
        dfs(0, [], 0)
        return res
