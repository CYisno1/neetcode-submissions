class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        count = n

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
            if union(a, b): # 成功 union 代表：原本兩個不同 component → 合併成一個，所以 component 數量少 1
                count -= 1
            # 不能 union 代表：a、b 本來就已經在同一個 component。
        
        return count
