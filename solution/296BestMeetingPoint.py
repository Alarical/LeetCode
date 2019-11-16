class Solution:
    """
    @param grid: a 2D grid
    @return: the minimize travel distance
    """
    def minTotalDistance(self, grid):
        # Write your code here
        rows = []
        cols = []
        m = len(grid)
        n = len(grid[0])
        if m == 0 :
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        rows.sort()
        cols.sort()
        ans = 0
        j = len(rows)-1
        i = 0
        while i < j :
            ans += rows[j] - rows[i]
            ans += cols[j] - cols[i]
            i+=1
            j-=1
        return ans
