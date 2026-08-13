class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i : [] for i in range(n)}

        for a, b in edges: # bc undirect, have to add both a and b
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                # 我要去 neighbor，所以現在的 node 就會變成它的 parent。
                if not dfs(neighbor, node):
                    return False
                
            return True

        # 檢查有沒有 cycle
        if not dfs(0, -1):
            return False
        
        # 檢查是不是全部 connected
        return len(visited) == n

        

