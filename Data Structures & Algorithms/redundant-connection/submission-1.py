class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # nodes 是 1 ~ n
        n = len(edges)

        # 一開始每個 node 都是自己的 parent
        parent = [i for i in range(n + 1)]

        # 找 x 所屬 component 的 root
        def find(x):
            while x != parent[x]:
                x = parent[x]

            return x

        # 把 a 和 b 所屬的兩組合併
        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            # 如果 root 一樣
            # 代表 a 和 b 原本就已經 connected
            if root_a == root_b:
                return False

            # 否則把兩組合併
            parent[root_b] = root_a

            return True

        # 按照 input 順序處理每條 edge
        for a, b in edges:

            # 如果 union 失敗
            # 代表 a 和 b 原本就在同一組
            # 再加這條 edge 就會形成 cycle
            if not union(a, b):
                return [a, b]   