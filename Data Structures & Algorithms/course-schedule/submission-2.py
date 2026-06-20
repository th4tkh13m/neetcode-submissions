class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # We do Kahn algorithm
        # Check the indegree first
        # If indegree = 0, add to queue
        # If no indeg = 0 => return False

        in_deg_map = {i: 0 for i in range(numCourses)}
        adj_list = {i: [] for i in range(numCourses) }
        visit = set()

        # Get indeg
        for course, preq in prerequisites:
            in_deg_map[course] = in_deg_map[course] + 1
            adj_list[preq].append(course)

        queue = deque([])
        
        for course, in_deg in in_deg_map.items():
            if in_deg == 0:
                queue.append(course)
                visit.add(course)

        while queue:
            course = queue.popleft()

            for neighbor in adj_list[course]:
                if not neighbor in visit:
                    in_deg_map[neighbor] -= 1

            for course, deg in in_deg_map.items():
                if deg == 0 and not course in visit:
                    queue.append(course)
                    visit.add(course)
        return len(visit) == numCourses