class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = [] # res[-1]: 目前已經合併好的最後一個 interval

        for start, end in intervals:
            # res 是空的，先放第一個
            if not res:
                res.append([start, end])
            
            # current start <= previous end -> overlap
            elif start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
                # ex: res[-1] = [1, 3], current = [2, 6] -> merged: [1, 6]
            
            # no overlap
            else:
                res.append([start, end])
        
        return res

                
