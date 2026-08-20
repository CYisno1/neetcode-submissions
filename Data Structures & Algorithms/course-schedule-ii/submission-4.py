class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
                
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    

                
        if len(res) != numCourses:
            return []
        
        return res