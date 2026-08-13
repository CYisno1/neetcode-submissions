class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[pre].append(course)
        
        # visiting: 現在這條 DFS path 裡的課程 ＝ 如果再次遇到 → cycle
        # visited: 以前已經完整檢查過，而且確定沒有 cycle = 再遇到可以直接跳過
        visiting = set()
        visited = set()

        def dfs(course):
            # 如果 course 正在目前 DFS path
            # => cycle
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            
            visiting.remove(course)
            visited.add(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True
            

