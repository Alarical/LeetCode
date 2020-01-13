class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self):
                self.par = list(range(100001))
            def find(self,x):
                if self.par[x] != x:
                    self.par[x] = self.find(self.par[x])
                return self.par[x]
            def union(self,x , y):
                xr , yr = self.find(x) , self.find(y)
                if xr == yr:
                    return False
                self.par[xr] = yr
                return True
        if n > len(connections) + 1:
            return -1
        uf = UnionFind()
        connections.sort(key = lambda x:x[0])
        for e in connections:
            uf.union(e[0] , e[1])
        ans = set()
        for i in range(n):
            par = uf.find(i)
            if par not in ans:
                ans.add(par)

        return len(ans) - 1
