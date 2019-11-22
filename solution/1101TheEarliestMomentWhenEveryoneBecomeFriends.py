class DSU(object):
    def __init__(self , n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self , x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self,x,y):
        par_x = self.find(x)
        par_y = self.find(y)
        if par_x == par_y:
            return
        if self.rank[par_x] < self.rank[par_y]:
            par_x , par_y = par_y , par_x
        self.par[par_y] = par_x
        self.rank[par_x] += self.rank[par_y]


class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        dsu = DSU(N)
        logs.sort()
        for log in logs:
            x = log[1]
            y = log[2]
            dsu.union(x,y)
            if dsu.rank[dsu.find(x)] == N:
                return log[0]
        return -1