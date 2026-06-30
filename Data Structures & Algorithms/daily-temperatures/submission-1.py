class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i

            stack.append(i)
        
        return res

"""
如果今天比 stack top 那天熱：
    那 stack top 那天的答案就是 i - prev_i
    pop 掉它

最後把今天也放進 stack，因為今天自己也要等未來更熱的一天
"""