class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        if len(self.small) > len(self.large) + 1:
            number = -heapq.heappop(self.small)
            heapq.heappush(self.large, number)
        
        elif len(self.large) > len(self.small):
            number = heapq.heappop(self.large)
            heapq.heappush(self.small, -number)
            
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
        