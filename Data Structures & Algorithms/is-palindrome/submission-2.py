class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        s_len = len(s)

        #abba
        if s_len % 2 != 0:
            mid = s_len // 2
            left = mid - 1
            right = mid + 1

            while left >= 0 and right < s_len:
                if s[left] != s[right]:
                    return False
                else:
                    left -= 1
                    right += 1
            
        else:
            left = (s_len // 2) - 1
            right = s_len // 2

            while left >= 0 and right < s_len:
                if s[left] != s[right]:
                    return False
                
                else:
                    left -= 1
                    right += 1
        
        return True
        