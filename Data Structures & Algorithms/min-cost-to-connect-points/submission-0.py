class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # 1. Build every possible edges
        edges = []

        for i in range(n): # i, j 是第幾個node
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                cost = abs(x1 - x2) + abs(y1 - y2)

                edges.append((cost, i, j)) # cost要在最前面因為等一下要照cost大小sort
        
        # 2. Cheapest edges first
        edges.sort()
        
        # 3. Union Find
        parent = list(range(n))

        def find(x):
            while x != parent[x]:
                x = parent[x]            
            return x
        
        def union(a, b):
            roota = find(a)
            rootb = find(b)

            if roota == rootb:
                return False
            
            parent[rootb] = roota
            return True
        
        # 4. Kruskal
        total_cost = 0
        edge_used = 0

        for cost, a, b in edges:
            if union(a, b): # 如果 union 成功就拿這條 edge
                total_cost += cost
                edge_used += 1
            
            if edge_used == n - 1: # 拿滿 n - 1 條就完成
                break
        
        return total_cost
