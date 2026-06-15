class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Find the rotten fruits
        n_rows, n_cols = len(grid), len(grid[0])
        queue = []
        list_bananas = set()
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] in [1,2]:
                    list_bananas.add((i,j))
        if not list_bananas:
            return 0
        minute = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            found_fresh = False
            for i in range(len(queue)):
                r, c = queue.pop(0)
                if grid[r][c] == 1:
                    found_fresh = True
                grid[r][c] = 2
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if 0 <= new_r < n_rows and\
                    0 <= new_c < n_cols and \
                    grid[new_r][new_c] == 1:
                        queue.append((new_r, new_c))
            if found_fresh:          
                minute += 1
        
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1:
                    return -1
        return minute               
                
