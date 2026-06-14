class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        visit = set()

        areas = []

        def dfs(row, col):
            area = 0
            stack = [(row, col)]

            while stack:
                # print(stack)
                i, j = stack.pop()
                
                
                directions = [[0,0], [1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    if 0 <= i + dr < n_rows \
                    and 0 <= j + dc < n_cols \
                    and not (i + dr, j + dc) in visit \
                    and grid[i + dr][j + dc] == 1:
                        visit.add((i + dr, j + dc))
                        area += 1
                        stack.append((i + dr, j + dc))
            areas.append(area)



        for row in range(n_rows):
            for col in range(n_cols):
                if not (row, col) in visit and grid[row][col] == 1:
                    dfs(row, col)

        return max(areas) if areas else 0       