class DSU:
    def __init__(self):
        self.par = list(range(5001)) # 初始化时父亲结点指向自身
        self.rnk = [0] * 5001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = DSU()
        for e in edges:
            # 判断有没有环
            if(uf.union(e[0], e[1]) == False):
                return False

        # 图可能没有连通，例如[[1, 2], [3, 4]]
        # 需要判断是不是所有节点的父亲都一样
        par = uf.find(0)
        for i in range(1, n):
            if par != uf.find(i):
                return False
        return True