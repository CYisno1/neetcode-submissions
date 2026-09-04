class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m = len(num1)
        n = len(num2)

        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])

                mul = digit1 * digit2

                p = i + j
                q = i + j + 1

                total = res[q] + mul

                res[q] = total % 10
                res[p] += total // 10
                
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
        
        return "".join(str(digit) for digit in res[start:])     
        