class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 先按照 end 從小到大排序，優先保留最早結束的 interval (greedy)
        # 如果後面的 interval 跟它 overlap，就刪掉後面的那個。
        intervals.sort(key = lambda x : x[1])

        remove = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                remove += 1
            
            else:
                prev_end = end
            # current 現在成為我們最新保留的 interval
        
        return remove