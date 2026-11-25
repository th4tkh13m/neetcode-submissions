class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Flatten matrix
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid // cols][mid % cols] == target:
                return True
            elif target < matrix[mid // cols][mid % cols]:
                right = mid - 1
            else:
                left = mid + 1
        return False