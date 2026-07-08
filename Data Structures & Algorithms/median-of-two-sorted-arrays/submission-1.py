class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(A) > len(B):
            A, B = B, A
        
        # m 是短 array 的長度
        # n 是長 array 的長度
        m = len(A)
        n = len(B)

        total = m + n

        half = (total + 1) // 2

        left = 0
        right = m

        while left <= right:
            # i 代表 A 左半邊要放幾個元素。
            i = (left + right) // 2
            # j 代表 B 左半邊要放幾個元素。
            j = half - i

            # 找出切線左右兩邊的邊界值。
            # Aleft  是 A 左半邊最大的數
            # Aright 是 A 右半邊最小的數
            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

             # 判斷目前切法合不合法。
            if Aleft <= Bright and Bleft <= Aright:
                # total是奇數
                if total % 2 == 1:
                    return max(Aleft, Bleft)
                else: # total是偶數
                    leftmax = max(Aleft, Bleft)
                    rightmin = min(Aright, Bright)
                    return (leftmax + rightmin) / 2
            
            # A 左邊放太多大數字了
            # 所以 i 要變小。
            elif Aleft > Bright:
                right = i - 1
            
            # 否則就是 Bleft > Aright
            # 代表 A 左邊放太少了
            # 所以 i 要變大
            else:
                left = i + 1


