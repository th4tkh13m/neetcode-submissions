class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n_rows, n_cols = len(grid), len(grid[0])

        # visit = set()
        queue = deque([])

        # Scan for the treasure chest first
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    # visit.add((row, col))
        current_level = 0
        directions = [(1,0), (-1,0), (0,1), (0, -1)]

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                # grid[row][col] = current_level

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    if 0 <= new_row < n_rows and 0 <= new_col < n_cols and grid[new_row][new_col] == 2147483647:
                        queue.append((new_row, new_col))

                        grid[new_row][new_col] = grid[row][col] + 1
        
        
