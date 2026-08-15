class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
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

            max_time = max(max_time, time)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    new_time = time + weight
                    heapq.heappush(min_heap, (new_time, neighbor))
                    
        
        if len(visited) == n:
            return max_time
        
        return -1