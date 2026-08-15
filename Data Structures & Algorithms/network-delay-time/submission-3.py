class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 從 k 發出訊號，訊號會沿著不同的路傳出去。我每次都先處理「最快能收到訊號的 node」
        graph = {i: [] for i in range(1, n + 1)}

        for u, v, t in times:
            graph[u].append((v, t))
        
        min_heap = [(0, k)]

        visited = set()
        max_time = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            if node in visited:
                continue
            
            visited.add(node)
            # 這個 node 最早收到訊號的時間已經確定了

            max_time = max(max_time, time)
            # 多久之後所有 nodes 都收到訊號

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    new_time = time + weight
                    heapq.heappush(min_heap, (new_time, neighbor))
                    
        
        if len(visited) == n:
            return max_time
        
        return -1