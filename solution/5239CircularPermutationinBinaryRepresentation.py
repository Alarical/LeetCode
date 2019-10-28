class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        import sys
        sys.setrecursionlimit(100000)
        def dfs(n , cur , ans , visited):
            if len(ans) == (1<<n):
                temp = ans[0] ^ ans[-1]
                return (temp & (temp-1)) == 0
            for i in range(n):
                other = cur ^ (1<<i)
                if other not in visited:
                    visited.add(other)
                    ans.append(other)
                    if dfs(n,other,ans,visited):
                        return True
                    visited.remove(other)
                    ans.remove(other)
            return False


        ans = []
        ans.append(start)
        visited = set()
        visited.add(start)
        dfs( n , start , ans , visited)
        return ans