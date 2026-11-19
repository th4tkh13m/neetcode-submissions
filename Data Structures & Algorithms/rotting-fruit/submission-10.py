class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        min_count = -1
        queue = deque([])

        # Search all rotten:
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if new_r < ROWS and new_r >= 0 and new_c < COLS and new_c >= 0 and grid[new_r][new_c] == 1:
                        queue.append((new_r, new_c))
                        grid[new_r][new_c] = 2
            min_count += 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
                
        
        return max(min_count, 0)




