class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        right:一直往右找,直到 window 包含 t
        left:一旦包含 t,就往右縮,縮到不能再縮
        """
        if len(t) > len(s):
            return ""

        need = defaultdict(int)
        for ch in t:
            need[ch] += 1

        window = defaultdict(int)

        have = 0
        need_types = len(need)

        res = ""
        res_len = float("inf")

        left = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                have += 1
            
            while have == need_types:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res = s[left:right + 1]
                
                left_ch = s[left]
                window[left_ch] -= 1

                # 如果移除 left_ch 後，某個必要字母不夠了
                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                left += 1
        
        return res
