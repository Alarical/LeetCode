#BFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [ 0 for _ in range(numCourses)]
        neighbor = [ [] for _ in range(numCourses) ]
        ans = []
        queue = []
        for depend in prerequisites:
            inDegree[depend[0]] += 1
            neighbor[depend[1]].append(depend[0])
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        while queue:
            cur_class = queue.pop()
            ans.append(cur_class)
            for next_class in neighbor[cur_class]:
                inDegree[next_class] -= 1
                if inDegree[next_class] == 0:
                    queue.append(next_class)
        return ans if len(ans) == numCourses else []

#DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(cur , visited, isLooped , graph , ans):
            if isLooped[cur] == 1:
                return False
            isLooped[cur] = 1
            for nxt in graph[cur]:
                if visited[nxt] == 0 and not dfs(nxt, visited, isLooped , graph , ans):
                    return False
            isLooped[cur] = 0
            visited[cur] = 1
            ans.append(cur)
            return True

        visited = [0 for _ in range(numCourses)]
        isLooped = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        ans = []
        for cur,nxt in prerequisites:
            graph[cur].append(nxt)
        for i in range(numCourses):
            if visited[i] == 0 and not dfs(i, visited, isLooped , graph , ans):
                return []
        print (ans)
        return ans if len(ans) == numCourses else []
