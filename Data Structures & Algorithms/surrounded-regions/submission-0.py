class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Loop thru the grid: check for Os
        # Do DFS for all the O's also store the locations
        # if no edge => flip everyone at once

        n_rows, n_cols = len(board), len(board[0])
        visit = set()

        def dfs(row, col):
            if row in (n_rows - 1,0) or col in (n_cols - 1, 0):
                return
            o_locs = set()
            stack = [(row, col)]
            o_locs.add((row, col))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while stack:
                i, j = stack.pop()
                for dr, dc in directions:
                    new_row, new_col = i + dr, j + dc
                    if 0 <= new_row < n_rows and 0 <= new_col < n_cols and board[new_row][new_col] == "O" and not (new_row, new_col) in o_locs:
                        if new_row in (n_rows - 1,0) or new_col in (n_cols - 1, 0):
                            return
                        stack.append((new_row, new_col))
                        o_locs.add((new_row, new_col))
                        visit.add((new_row, new_col))
            for i, j in o_locs:
                board[i][j] = "X"

            

        for row in range(n_rows):
            for col in range(n_cols):
                if board[row][col] == "O" and not (row, col) in visit:
                    # maybe we check for visit for efficiency
                    visit.add((row, col))
                    dfs(row, col)
                