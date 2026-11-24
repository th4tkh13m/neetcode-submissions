class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Firstly do binary search by rows:
        # Just find the row that contains target
        m,n = len(matrix), len(matrix[0])

        left = 0
        right = m - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if matrix[mid][n-1] == target:
                return True
            elif matrix[mid][n-1] < target:
                left = mid +1
            elif matrix[mid][n-1] > target:
                right = mid - 1

        if target < matrix[mid][n-1]:
            row_num = mid
        else:
            row_num = mid + 1
            if row_num >= m:
                row_num = mid

        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if matrix[row_num][mid] == target:
                return True
            elif matrix[row_num][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
