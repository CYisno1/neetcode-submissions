class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = Counter(s)
        countT = Counter(t)

        for key, value in countS.items():
            if key in countT:
                if value != countT[key]:
                    return False
            else:
                return False
        
        return True

        