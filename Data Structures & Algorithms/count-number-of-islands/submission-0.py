class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        def dfs(i, j, grid):
            # We can do horizontally or vertically
            stack = [(i,j)]
            new_grid = grid
            while stack:
                row, col = stack.pop()
                new_grid[row][col] = 0
                # Explore the 4 directions:
                if row - 1 >= 0 and new_grid[row-1][col] == "1":
                    stack.append((row-1, col))
                if row + 1 < num_rows and new_grid[row+1][col] == "1":
                    stack.append((row+1, col))
                if col - 1 >= 0 and new_grid[row][col-1] == "1":
                    stack.append((row, col-1))
                if col + 1 < num_cols and new_grid[row][col+1] == "1":
                    stack.append((row, col+1))
            return new_grid

        count = 0
        for row in range(num_rows):
            for col in range(num_cols):
                # print(grid[row][col], grid[row][col] == 1)
                if grid[row][col] == "1":
                    # print("HERE")
                    # Do DFS to flip all the 0s
                    grid = dfs(row, col, grid)
                    count += 1
        return count
