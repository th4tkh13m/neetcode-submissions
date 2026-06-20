class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # If zero fruit => 0
        # If zero fresh => 0
        n_rows, n_cols = len(grid), len(grid[0])
        queue = deque([])
        
        # Scan for rotten fruits
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            changed = False
            # Per level search
            for i in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    if 0 <= new_row < n_rows and 0 <= new_col < n_cols and grid[new_row][new_col] == 1:
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 2
                        changed = True
            if changed:
                minutes += 1
            
        
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 1:
                    return -1
        return minutes

