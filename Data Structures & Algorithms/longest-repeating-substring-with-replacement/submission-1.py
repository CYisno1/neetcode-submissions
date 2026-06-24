class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = defaultdict(int)
        res = 0
        max_count = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]]) # window 裡最多的字母數

            # 需要替換的字母數 = window 長度 - window 裡最多的字母數
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        
        return res
            
                
            
            