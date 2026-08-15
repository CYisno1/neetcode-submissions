class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}

        def dfs(current, target, visited):
            if current == target:
                return True
            
            visited.add(current)

            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            
            return False
        
        for a, b in edges:
            visited = set()
            
            if a in graph and b in graph and dfs(a, b, visited):
                return [a, b]
            
            if a not in graph:
                graph[a] = []
            
            if b not in graph:
                graph[b] = []

            graph[a].append(b)
            graph[b].append(a)