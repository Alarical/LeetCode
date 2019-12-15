class UnionFind:
    def __init__(self):
        self.par = list(range(5001))
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


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind()
        for e in edges:
            uf.union(e[0] , e[1])
        ans = set()
        for i in range(n):
            par = uf.find(i)
            if par not in ans:
                ans.add(par)
        return len(ans)