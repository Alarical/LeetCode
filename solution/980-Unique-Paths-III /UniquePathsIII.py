class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(x, y, zerocount):
            direction = [(-1,0),(1,0),(0,1),(0,-1)]
            for i,j in direction:
                nx ,ny = x+i , y+j
                if 0 <= nx < m and 0 <=ny < n:
                    if grid[nx][ny] == 2:
                        if zerocount == 0:
                            self.res += 1
                            return
                        else:
                            continue
                    if grid[nx][ny] == 0: # backtracking
                        grid[nx][ny] = 1
                        dfs(nx, ny , zerocount-1)
                        grid[nx][ny] = 0

       
        m , n  = len(grid),len(grid[0])
        zerocount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx , sy = i,j
                elif grid[i][j] == 2:
                    end = (i,j)
                elif grid[i][j] == 0:
                    zerocount += 1
        self.res = 0       
        dfs(sx , sy , zerocount)
        return self.res
    
A = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]   
print (Solution().uniquePathsIII(A))