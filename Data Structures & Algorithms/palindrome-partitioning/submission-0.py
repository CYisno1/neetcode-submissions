class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current = []

        # start 固定這一層從哪裡開始，而 end 用來嘗試這一刀切在哪裡。
        def dfs(start):
            if start == len(s):
                res.append(current.copy())
                return
            
            for end in range(start, len(s)):
                substring = s[start: end + 1]

                if substring == substring[:: -1]:
                    current.append(substring)
                    dfs(end + 1)
                    current.pop()
        
        dfs(0)
        return res

