class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        max_area = 0

        # visit = set()

        def dfs(i, j):
            directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

            stack = [(i,j)]
            # visit.add((i,j))
            current_area = 0
            grid[i][j] = 0
            while stack:
                row, col = stack.pop()
                current_area += 1
                

                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if 0 <= new_r < n_rows and 0 <= new_c < n_cols and grid[new_r][new_c] == 1:
                        stack.append((new_r, new_c))
                        grid[new_r][new_c] = 0

            
            nonlocal max_area
            max_area = max(current_area, max_area)

                

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1:
                    dfs(i, j)
               
        
        return max_area