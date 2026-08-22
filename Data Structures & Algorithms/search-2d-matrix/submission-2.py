class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Double binary search through rows then column

        # Row binary search
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                return True
        
        # When the while loop breaks, that means c will be smaller than r
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[bottom][mid] > target:
                r = mid - 1
            elif matrix[bottom][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False
