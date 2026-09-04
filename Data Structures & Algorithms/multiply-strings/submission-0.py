class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 特殊情況：任何數 × 0 = 0
        if num1 == "0" or num2 == "0":
            return "0"
        
        m = len(num1)
        n = len(num2)

        # m 位數 × n 位數，答案最多 m + n 位
        # 例如 99 × 99 = 9801 → 2 + 2 = 4 位
        res = [0] * (m + n)

        # 從右往左做直式乘法
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])

                # 目前兩個 digit 相乘
                mul = digit1 * digit2

                # 乘積會影響 res 的這兩個位置
                # p2 放個位數
                # p1 放 carry
                p1 = i + j
                p2 = i + j + 1

                # res[p2] 可能已經有前面乘法留下來的值
                # 所以不是只有 mul，要加上原本的 res[p2]
                total = mul + res[p2]

                # 例如 total = 27
                # 個位數 7 放在 p2
                res[p2] = total % 10

                # carry 2 加到前面的 p1
                res[p1] += total // 10
        
        # res 最前面可能有沒用到的 0
        # 例如 [0, 5, 5, 3, 5]
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1

        # [5,5,3,5] → "5535"
        return "".join(str(digit) for digit in res[start:])