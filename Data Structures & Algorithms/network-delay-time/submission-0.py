import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i : [] for i in range(1, n+1)}

        # 1. 建 adjacency list
        # graph[node] = [(neighbor, weight), ...]
        for u, v, t in times:
            graph[u].append((v, t))

        # 2. min heap
        # 每個 element = (目前從 k 到這個 node 的時間, node)
        min_heap = [(0, k)] # 起點k到自己是0秒

        visited = set() # 這個 node 的 shortest distance 已經確定了
        max_time = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            
            visited.add(node)

            max_time = max(max_time, time)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    new_time = time + weight
                    heapq.heappush(min_heap, (new_time, neighbor))
        
        if len(visited) == n:
            return max_time
        
        return -1


        

        