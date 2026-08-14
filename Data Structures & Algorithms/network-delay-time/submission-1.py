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

            # 目前確定的 shortest distance 中最大的
            # 大家都走完需要看最慢的那個需要多少時間
            max_time = max(max_time, time)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    # k -> ... -> node -> neighbor
                    new_time = time + weight
                    heapq.heappush(min_heap, (new_time, neighbor)) # 注意：這裡是 neighbor！
                    # 找到一條到 neighbor 距離是 new_time 的路，把它放進 heap
        
        # 所有 nodes 都能從 k 到達
        if len(visited) == n:
            return max_time
        
        return -1


        

        