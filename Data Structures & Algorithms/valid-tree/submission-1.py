class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build undirected graph
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            # 已經走過就不用再走
            if node in visited:
                return

            visited.add(node)

            # 走所有 neighbors
            for neighbor in graph[node]:
                dfs(neighbor)

        # 從任意一個 node 開始
        dfs(0)

        # 如果全部 n 個 nodes 都能從 0 走到
        # => connected
        return len(visited) == n  