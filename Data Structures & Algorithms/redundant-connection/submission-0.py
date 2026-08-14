class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        # 對於每一條 [a, b]，在把它加進 graph 之前，先檢查 a 能不能已經走到 b

        visited = set()

        # 檢查：從 current 出發，能不能走到 target
        def dfs(current, target, visited):
            # 如果已經走到 target
            # 代表 current 和 target 本來就已經 connected
            if current == target:
                return True
            
            visited.add(current)

            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            
            # 全部路都走完，還是找不到 target
            return False
        
        # 一條一條處理 edge
        for a, b in edges:

            # 每次檢查一條新的 edge，
            # visited 都要重新開始
            visited = set()

            # 如果 a 和 b 已經都存在 graph 中，
            # 而且 a 已經可以走到 b
            if a in graph and b in graph and dfs(a, b, visited): # dictionary.get(key, default_value)
                return [a, b]
            
            # 沒有形成 cycle
            # 才正式把這條 edge 加進 graph
            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []

            graph[a].append(b)
            graph[b].append(a)
                

            

            

        
