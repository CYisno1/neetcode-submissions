class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[pre].append(course)
        
        visiting = set()
        visited = set()

        # 從這堂 course 繼續往後修，會不會遇到 prerequisite cycle？
        def dfs(course):
            # 如果我正在走這條路，結果又走回目前路徑上的 course，代表有 cycle。
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            visited.add(course)
            visiting.remove(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
                
            
            