class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = [0] * 26

        # 先建立 s1 的 frequency
        for ch in s1:
            ind = ord(ch) - ord("a")
            count1[ind] += 1

        # 先建立 s2 第一個 window 的 frequency
        count2 = [0] * 26
        for i in range(len(s1)):
            ind2 = ord(s2[i]) - ord("a")
            count2[ind2] += 1
        
        if count1 == count2:
            return True
        
        left = 0
        # right 從 len(s1) 開始，代表新的字進 window
        for right in range(len(s1), len(s2)):
            ind_r = ord(s2[right]) - ord("a")
            count2[ind_r] += 1

            ind_l = ord(s2[left]) - ord("a")
            count2[ind_l] -= 1

            left += 1

            if count1 == count2:
                return True
        
        return False







