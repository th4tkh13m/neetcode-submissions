class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n_rows, n_cols = len(grid), len(grid[0])
        queue = []
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        

        # Do BFS
        # visit = set()
        dist = 0
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            print(queue)
            for i in range(len(queue)):
                r, c = queue.pop(0)
                if grid[r][c] == 2147483647:
                    grid[r][c] = dist
                for dr, dc in direction:
                    new_r = r + dr
                    new_c = c + dc
                    if 0 <= new_r < n_rows and 0 <= new_c < n_cols and grid[new_r][new_c] == 2147483647:
                        queue.append((new_r, new_c))
                
            dist += 1
        

