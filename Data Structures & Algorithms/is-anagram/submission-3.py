class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}

        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1
        
        count_t = {}

        for char in t:
            if char not in count_s:
                return False
            
            if char in count_t:
                count_t[char] += 1
            
            else:
                count_t[char] = 1
            
    
        return count_t == count_s
