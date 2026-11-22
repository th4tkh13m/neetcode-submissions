class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First check rows
        for row in board:
            check = set()
            for val in row:
                if val != ".":
                    if not val in check:
                        check.add(val)
                    else:
                        return False
        

        # Check column
        for col in range(9):
            check = set()
            for row in range(9):
                val = board[row][col]
                if val != ".":
                    if not val in check:
                        check.add(val)
                    else:
                        return False
        

        # Check box
        for row_box in range(0,9,3):
            for col_box in range(0,9,3):
                check = set()
                for row in range(row_box, row_box+3):
                    for col in range(col_box, col_box+3):
                        val = board[row][col]
                        if val != ".":
                            if not val in check:
                                check.add(val)
                            else:
                                return False
        return True

            
