class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        visit = set()

        max_area = 0

        def dfs(row, col, max_area):
            area = 0
            stack = [(row, col)]

            directions = [[0,0], [1,0], [-1,0], [0,1], [0,-1]]
            while stack:
                # print(stack)
                i, j = stack.pop()
                
                
                for dr, dc in directions:
                    if 0 <= i + dr < n_rows \
                    and 0 <= j + dc < n_cols \
                    and not (i + dr, j + dc) in visit \
                    and grid[i + dr][j + dc] == 1:
                        visit.add((i + dr, j + dc))
                        area += 1
                        stack.append((i + dr, j + dc))
            if area > max_area:
                max_area = area
            return max_area


        for row in range(n_rows):
            for col in range(n_cols):
                if not (row, col) in visit and grid[row][col] == 1:
                    max_area = dfs(row, col, max_area)

        return max_area      