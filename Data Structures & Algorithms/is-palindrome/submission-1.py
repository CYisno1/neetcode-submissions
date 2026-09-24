class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers!
        left = 0
        right = len(s) - 1

        while left < right:
            # 找到alphanumeric character再開始比較
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True


