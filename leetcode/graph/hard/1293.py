class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        que = list()
        row = len(grid)
        col = len(grid[0])
        #   steps,i,j,remainder
        que = deque([(0,0,0,k)])
        seen=dict()
        seen[(0,0,0,k)]=1
        while que:
            (step,i,j,remainder) = que.popleft()
            if i==row-1 and j==col-1:
                return step
            for newI,newJ in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                if newI >= 0 and newI < row and newJ >= 0 and newJ < col:
                    newRemainer = remainder-grid[newI][newJ]
                    if newRemainer >= 0 and (newI,newJ,newRemainer) not in seen:
                        que.append((step+1,newI,newJ,newRemainer))
                        seen[(newI,newJ,newRemainer)]=1
        return -1