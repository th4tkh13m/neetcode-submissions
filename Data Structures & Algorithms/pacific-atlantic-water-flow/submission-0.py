class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Store the position hashmap -> True/False for being able to reach the sea
        # If BFS reach some of this, we would return faster
        # If we only have 1 row, 1 col, then we return all?
        
        pacific_map = set()
        atlantic_map = set()
        n_rows, n_cols = len(heights), len(heights[0])
        # if n_rows == 1 or n_cols == 1:
            # return heights
        
        queue_atlantic = deque([])
        queue_pacific = deque([])

        # Curate initial maps
        for i in range(n_rows):
            for j in range(n_cols):
                if i == 0 or j == 0:
                    pacific_map.add((i, j))
                    queue_pacific.append((i,j))
                if i == n_rows - 1 or j == n_cols - 1:
                    atlantic_map.add((i, j))
                    queue_atlantic.append((i,j))
        print(queue_pacific)
        print(queue_atlantic)

        def bfs(queue, visit_map):
            directions = [(1,0), (-1,0), (0,1), (0, -1)]
            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()

                    for dr, dc in directions:
                        new_row, new_col = row + dr, col + dc

                        if 0 <= new_row < n_rows and 0 <= new_col < n_cols and heights[new_row][new_col] >= heights[row][col] \
                        and not (new_row, new_col) in visit_map:
                            queue.append((new_row, new_col))
                            visit_map.add((new_row, new_col))
            return visit_map

        atlantic_map = bfs(queue_atlantic, atlantic_map)
        pacific_map = bfs(queue_pacific, pacific_map)

        return list(atlantic_map.intersection(pacific_map))

                

        
