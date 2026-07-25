class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # For even length, we take max value for left and
        # min value for right.
        # Applying this to 2 arrays, we take the max of the
        # 2 lower halves and min of the 2 upper halves
        A = nums1
        B = nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Ensure A is the smaller array
        if len(B) < len(A):
            A, B = B, A

        left = 0
        right = len(A) - 1

        while True:
            mid_a = left + (right - left) // 2
            mid_b = half - mid_a - 2 # Idx to length for both arrays (off by 1)

            a_left = A[mid_a] if mid_a >= 0 else float("-inf")
            a_right = A[mid_a + 1] if mid_a + 1 < len(A) else float("inf")
            b_left = B[mid_b] if mid_b >= 0 else float("-inf")
            b_right = B[mid_b + 1] if mid_b + 1 < len(B) else float("inf")

            # Check if partitions for both arrays are correct
            if a_left <= b_right and b_left <= a_right:
                # Odd Case:
                if total % 2 == 1:
                    return min(a_right, b_right)
                
                # Even Case:
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            
            elif a_left > b_right:
                # If the left partion is bigger, then we need more elements in A
                right = mid_a - 1
            else:
                # Otherwise, the left partition is too big, shift right
                left = mid_a + 1
