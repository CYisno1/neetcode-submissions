class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
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
        
        for a, b in edges:
            if not union(a, b): # 如果這條 edge 無法正常 union，代表它會造成 cycle，所以整張 graph 不是 tree。
                return False
            
        return True