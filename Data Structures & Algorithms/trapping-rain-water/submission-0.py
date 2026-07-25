class Solution:
    def trap(self, height: List[int]) -> int:
        # Water trapped is defined as min(left, right)
        if height == None:
            return 0
        
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        res = 0

        while left < right:
            # Look at bottleneck
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                res += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                res += max_right - height[right]
        
        return res
            