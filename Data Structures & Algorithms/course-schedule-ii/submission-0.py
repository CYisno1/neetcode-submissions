class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[pre].append(course)
        
        visiting = set()
        visited = set()
        res = []

        def dfs(course): 
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            
            visited.add(course)
            visiting.remove(course)
            res.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        # 因為我們建立的是 pre → course
        # DFS postorder 是反過來的
        return res[::-1]   
            
