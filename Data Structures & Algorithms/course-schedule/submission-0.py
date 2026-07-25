class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjacency list for courses to prereq courses
        courseMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courseMap[course].append(prereq)
        
        # Store courses in DFS path
        visited = set()

        def dfs(course):
            if course in visited:
                # Cycle
                return False
            if courseMap[course] == []:
                return True
            
            # Otherwise, we check the nodes that it is connected to
            visited.add(course)
            for prereq in courseMap[course]:
                # Return False if returned False from prereq courses
                if not dfs(prereq):
                    return False
            # Reset visited
            visited.remove(course)

            # Clear current course prereq if the courses returns True
            courseMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        