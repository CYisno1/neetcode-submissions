class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0

        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)

        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        
        return count