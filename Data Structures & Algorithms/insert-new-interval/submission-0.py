class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # 三種情況

        for start, end in intervals:
            # interval 在 newInterval左邊
            if end < newInterval[0]:
                res.append([start, end])

            # interval 在 newInterval右邊
            elif start > newInterval[1]:
                res.append(newInterval)
                newInterval = [start, end] # 這邊的newInterval是指還沒放進答案的interval
            
            # interval 包在 newInterval裡面
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])

        # 所有 interval 都處理完，再把最後剩下的 newInterval 放進去    
        res.append(newInterval)
        return res

