class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        import heapq
        courses = sorted(courses , key = lambda x:x[1])
        queue = []
        cur_time = 0
        for cost,end in courses:
            if cur_time+cost <= end:
                heapq.heappush(queue , -cost)
                cur_time += cost
            elif queue and cost < -queue[0]:
                cur_time += cost + heapq.heappop(queue)
                heapq.heappush(queue,-cost)
        return len(queue)
