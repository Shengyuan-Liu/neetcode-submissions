class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        up, down = 0, m - 1
        while up < down:
            mid = (up + down + 1) // 2
            mid_v = matrix[mid][0]
            if mid_v > target:
                down = mid - 1
            elif mid_v < target:
                up = mid
            else:
                return True
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            mid_v = matrix[up][mid]
            if mid_v > target:
                right = mid - 1
            elif mid_v < target:
                left = mid + 1
            else:
                return True
        return False