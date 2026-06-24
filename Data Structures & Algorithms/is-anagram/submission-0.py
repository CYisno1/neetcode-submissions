class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sseen = defaultdict(int)
        tseen = defaultdict(int)
        
        for i in s:
            sseen[i] += 1
        
        for i in t:
            tseen[i] += 1
        
        if sseen == tseen:
            return True
        else:
            return False

        