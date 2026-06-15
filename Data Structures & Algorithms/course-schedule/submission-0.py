class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        # Do BFS
        # Find indegree
        in_degrees = {}
        adj_list = {}
        for u, v in prerequisites:
            if not u in in_degrees:
                in_degrees[u] = 0
                adj_list[u] = [v]
            else:
                adj_list[u].append(v)
            
            if not v in in_degrees:
                in_degrees[v] = 1
                adj_list[v] = []
            else:
                in_degrees[v] += 1
        queue = []
        visit = set()
        for node in in_degrees.keys():
            if in_degrees[node] == 0:
                queue.append(node)
                visit.add(node)
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                for neighbor in adj_list[node]:
                    if in_degrees[neighbor] > 0:
                        in_degrees[neighbor] -= 1
                        if in_degrees[neighbor] == 0 and not neighbor in visit:
                            queue.append(neighbor)
                            visit.add(neighbor)

        return visit == set(adj_list.keys())

            