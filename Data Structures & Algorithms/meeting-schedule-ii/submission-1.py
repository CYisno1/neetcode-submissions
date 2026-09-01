"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)

        min_heap = [] # 裝結束時間
        
        for interval in intervals:
            # 最早結束的 room 已經空了
            if min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)
            
            # 把目前 meeting 的 end 放進去
            heapq.heappush(min_heap, interval.end)
        
        return len(min_heap)