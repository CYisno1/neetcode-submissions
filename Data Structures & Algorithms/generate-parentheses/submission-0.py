class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(current, left, right):
            if len(current) == 2*n:
                res.append(current)
                return
            
            if left < n:
                dfs(current + "(", left + 1, right)
            
            if right < left:
                dfs(current + ")", left, right + 1)
        
        dfs("", 0, 0)
        return res
            
            