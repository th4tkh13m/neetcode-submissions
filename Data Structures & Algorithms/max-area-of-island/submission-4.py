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
                    if 0 <= i + dr < n_rows \
                    and 0 <= j + dc < n_cols \
                    and not (i + dr, j + dc) in visit \
                    and grid[i + dr][j + dc] == 1:
                        visit.add((i + dr, j + dc))
                        stack.append((i + dr, j + dc))
            if area > max_area:
                max_area = area
            return max_area


        for row in range(n_rows):
            for col in range(n_cols):
                if not (row, col) in visit and grid[row][col] == 1:
                    max_area = dfs(row, col, max_area)

        return max_area      