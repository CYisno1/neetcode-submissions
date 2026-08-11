class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        tmp = []

        if len(digits) == 0:
            return res

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

        def dfs(index):
            if len(tmp) == len(digits):
                res.append("".join(tmp))
                return

            for c in phone[digits[index]]:

                tmp.append(c)
                dfs(index + 1)
                tmp.pop()

        dfs(0)
        return res



