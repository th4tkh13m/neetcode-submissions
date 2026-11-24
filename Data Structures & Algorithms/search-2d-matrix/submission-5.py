class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n - 1


        while left <= right:
            mid = left + (right - left) // 2
            print(mid)
            if target == matrix[mid // n][mid % n]:
                return True
            elif target < matrix[mid // n][mid % n]:
                right = mid - 1
            else:
                left = mid + 1
        return False