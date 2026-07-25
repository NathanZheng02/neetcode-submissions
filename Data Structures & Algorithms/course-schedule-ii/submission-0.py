class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Adding to adjacency list
        adjList = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adjList[course].append(pre)
        
        res = []
        # Visited is for nodes that are seen. If a current
        # explored node is connected to an explored path, that means
        # it does not contain a cycle, hence the return True
        #
        # Cycle is resetted for each dfs rotation
        # to detect "cycles"
        visited = set()
        cycle = set()
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in adjList[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
    
