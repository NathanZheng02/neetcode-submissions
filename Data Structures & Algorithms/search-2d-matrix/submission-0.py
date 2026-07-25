class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Row search
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][0] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else: 
                return True
        
        # Look through each element in the row

        left = 0
        right = len(matrix[bottom]) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[bottom][mid] < target:
                left = mid + 1
            elif matrix[bottom][mid] > target:
                right = mid - 1
            else: 
                return True

        return False
