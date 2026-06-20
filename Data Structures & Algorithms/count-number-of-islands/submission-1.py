class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        n_rows, n_cols = len(grid), len(grid[0])
        visit = set()
        
        def dfs(i, j):
            directions = [(1,0), (-1,0), (0, 1), (0,-1)]

            stack = [(i,j)]

            
            while stack:
                row, col = stack.pop()
                grid[i][j] = "0"
                

                # loop thru directions and add to stack
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if 0 <= new_r < n_rows and 0 <= new_c < n_cols and not (new_r, new_c) in visit and grid[new_r][new_c] == "1":
                        stack.append((new_r, new_c))
                        visit.add((new_r, new_c))

        for i in range(n_rows):
            for j in range(n_cols):
                if not (i,j) in visit and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count