class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        visit = set()

        max_area = 0

        def dfs(row, col, max_area):
            area = 0
            stack = [(row, col)]
            visit.add((row, col))

            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            while stack:
                # print(stack)
                i, j = stack.pop()
                area += 1
                
                for dr, dc in directions:
                    new_i, new_r = i + dr, j + dc
                    if 0 <= new_i < n_rows \
                    and 0 <= new_r < n_cols \
                    and not (new_i,new_r ) in visit \
                    and grid[new_i][new_r] == 1:
                        visit.add((new_i, new_r))
                        stack.append((new_i, new_r))
            if area > max_area:
                max_area = area
            return max_area


        for row in range(n_rows):
            for col in range(n_cols):
                if not (row, col) in visit and grid[row][col] == 1:
                    max_area = dfs(row, col, max_area)

        return max_area      