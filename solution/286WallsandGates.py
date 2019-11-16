class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        m = len(rooms)
        if m == 0:
            return []
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    self.dfs(rooms , i , j , 0 , m , n)
        return rooms

    def dfs(self , rooms , i , j , val , m , n):
        if i < 0 or i >= m  or j < 0 or j >= n or rooms[i][j] < val:
            return
        rooms[i][j] = val
        self.dfs(rooms , i+1 , j , val+1 , m , n)
        self.dfs(rooms , i-1 , j , val+1 , m , n)
        self.dfs(rooms , i , j+1 , val+1 , m , n)
        self.dfs(rooms , i , j-1 , val+1 , m , n)
        return

