"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        dic = collections.defaultdict(int)

        for interval in intervals:
            dic[interval.start] += 1
            dic[interval.end] -= 1

        
        res = 0
        count = 0
        for key in sorted(dic.keys()):
            count += dic[key]

            res = max(res, count)

        return res