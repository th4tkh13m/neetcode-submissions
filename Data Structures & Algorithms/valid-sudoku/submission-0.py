class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for j in range(9):
            count_list = [0] * 9
            for i in range(9):
                val = board[i][j]
                
                if val != ".":
                    count_list[int(val) - 1] += 1
            # Check for count list
            for val in count_list:
                if val > 1:
               
                    return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                count_list = [0] * 9
                for j in range(3):
                    for i in range(3):
 
                        val = board[i + box_row ][j + box_col ]
                        
                        if val != ".":
                            count_list[int(val) - 1] += 1
                        
                # Check for count list
                for val in count_list:
                    if val > 1:
         
                        return False
        

        
        # Check row:
        for r in board:
            count_list = [0] * 9
            for val in r:
                if val != ".":
                    count_list[int(val) - 1] += 1
            
            # Check for count list
            for val in count_list:
                if val > 1:
                  
                    return False
        return True

        