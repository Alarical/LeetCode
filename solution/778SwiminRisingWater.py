class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        n = len(grid)
        queue = []  # python 小顶堆
        heapq.heappush(queue , (grid[0][0], 0*n + 0)) # x*n+y
        visited = [0]*(n**2)
        dirs = [-1,0,1,0,-1]
        visited[0] = 1
        while queue:
            pos = heapq.heappop(queue)
            t = pos[0]
            x = pos[1]//n
            y = pos[1]%n
            if x == n-1 and y == n-1:
                return t
            for i in range(4):
                tx = x + dirs[i]
                ty = y + dirs[i+1]
                if tx < 0 or tx >=n or ty < 0 or ty >= n:
                    continue
                if visited[tx*n+ty] == 1:
                    continue
                visited[tx*n+ty] = 1
                heapq.heappush(queue , (max(t,grid[tx][ty]) , tx*n+ty) )
        return -1



