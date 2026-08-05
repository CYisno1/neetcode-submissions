class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        current = []

        def dfs(i):
        # i: 現在走到digits的哪個數
            if i == len(digits):
                res.append("".join(current)) # "".join(current) 把 list 轉成一個新的 string
                                             # 且string immutable 所以不用加copy()
                return
            
            for ch in phone[digits[i]]:
                current.append(ch)
                dfs(i + 1)
                current.pop()
        
        dfs(0)
        return res

