class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        need = defaultdict(int)
        for ch in t:
            need[ch] += 1
        
        window = defaultdict(int) 

        have = 0
        need_type = len(need)

        res = ""
        res_len = float("inf")

        left = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                have += 1
            
            while have == need_type:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res = s[left:right + 1]
                
                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
                
                left += 1
        return res
            
        

        