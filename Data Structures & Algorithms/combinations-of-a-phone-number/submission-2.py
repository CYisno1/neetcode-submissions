class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []
        current = []

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

        def dfs(i):
            if i == len(digits):
                res.append("".join(current))
                return
            
            for ch in phone[digits[i]]:
                current.append(ch)
                dfs(i + 1)
                current.pop()
        
        dfs(0)
        return res

            