class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 要排除的是：不同 index 產生了內容完全相同的組合。
        candidates.sort()
        res = []

        def dfs(start, current, total):
            if total == target:
                res.append(current.copy())
                return
            
            for i in range(start, len(candidates)):
                num = candidates[i]

                # base case:
                if total + num > target:
                    break
                # 因為已經sort所以後面數只會更大 就不用再看後面的數了

                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # 跳過重複的數
                
                current.append(num)
                dfs(i + 1, current, total + num)
                current.pop()


        dfs(0, [], 0)
        return res