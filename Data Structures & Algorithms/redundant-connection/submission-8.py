class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(a, b):
            roota = find(a)
            rootb = find(b)

            if roota == rootb:
                return False
            
            # 把兩棵 tree 的 root 接起來。
            parent[rootb] = roota
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]