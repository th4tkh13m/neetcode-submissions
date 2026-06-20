class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_deg_map = {i: 0 for i in range(numCourses)}
        adj_list = {i: [] for i in range(numCourses) }
        visit = []

        # Get indeg
        for course, preq in prerequisites:
            in_deg_map[course] = in_deg_map[course] + 1
            adj_list[preq].append(course)

        queue = deque([])
        
        for course, in_deg in in_deg_map.items():
            if in_deg == 0:
                queue.append(course)
                visit.append(course)

        while queue:
            course = queue.popleft()

            for neighbor in adj_list[course]:
                if not neighbor in visit:
                    in_deg_map[neighbor] -= 1

            for course, deg in in_deg_map.items():
                if deg == 0 and not course in visit:
                    queue.append(course)
                    visit.append(course)
        return visit if len(visit) == numCourses else []