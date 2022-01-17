class Solution:
    def detectCycle(self,adj,visited,idx):
        if visited[idx] == 2:
            return True
        visited[idx] = 2
        for vertex in range(len(adj[idx])):
            if adj[idx][vertex] != -1 and visited[vertex] != 1:
                if self.detectCycle(adj,visited,vertex):
                    return True
        visited[idx] = 1
        return False
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[0]*numCourses for i in range(numCourses)]
        for i in range(numCourses):
            for j in range(numCourses):
                adj[i][j] = -1
        
        visited = [0 for i in range(numCourses)]
        for courses in prerequisites:
            a,b = courses[0],courses[1]
            adj[a][b] = 1
            
        for idx in range(numCourses):
            if self.detectCycle(adj,visited,idx):
                return False
            visited[idx] = 1
        return True