import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)

        # 保存 (剩餘次數, 可以再次執行的時間)
        queue = deque()
        time = 0

        while heap or queue:
            time += 1

            # 先把冷卻完成的 task 放回 heap
            if queue and queue[0][1] <= time:
                freq, available_time = queue.popleft()
                heapq.heappush(heap, freq)

            # 再選目前剩餘次數最多的 task
            if heap:
                freq = heapq.heappop(heap)
                freq += 1 # 因為 freq 是負數，+1 代表使用掉一次

                # 還有剩餘次數，就進入 cooldown
                if freq < 0:
                    queue.append((freq, time + n + 1))

        
        return time
