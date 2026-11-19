class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        n_rows, n_cols = len(grid), len(grid[0])

        visit = set()
        queue = deque([])

        for i in range(n_rows):
            for j in range(n_cols):
                if (i, j) in visit:
                    j += 1
                    continue
                visit.add((i, j))

                if grid[i][j] == "1":
                    num_islands += 1
                    queue.append((i, j))

                    while queue:
                        r, c = queue.popleft()
                        # Island (start bfs)
                        for dr, dc in [(0, -1), (0,1), (-1,0), (1, 0)]:
                            new_r, new_c = r + dr, c + dc
                            if  new_r >= 0 and new_r < n_rows and new_c >= 0 and new_c < n_cols and not (new_r, new_c) in visit:
                                visit.add((new_r, new_c))
                                if grid[new_r][new_c] == "1":
                                    queue.append((new_r, new_c))

        return num_islands
                                
