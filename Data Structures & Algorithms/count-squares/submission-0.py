from collections import defaultdict
class CountSquares:

    def __init__(self):
        # 一定要記「同一個點出現幾次」
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0

        # 把每個 existing point 當成可能的 diagonal point
        for (x2, y2), freq in self.points.items():
            if abs(x2 - x) != abs(y2 - y):                
                continue
            
            # 不能是同一條水平/垂直線，否則沒有面積
            if x2 == x or y2 == y:
                continue
            
            # 另外兩個 corner
            corner1 = x2, y
            corner2 = x, y2

            # 三個 existing corners 的出現次數相乘
            ans += (
                freq
                * self.points.get(corner1, 0)
                * self.points.get(corner2, 0)
            )
            # 如果 corner1 或 corner2 原本不存在，defaultdict 會自動幫你建立 corner1: 0
            # 就會出現：RuntimeError: dictionary changed size during iteration
            # 所以用 .get()就不會新增 key
        
        return ans

        
