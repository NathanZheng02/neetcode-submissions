class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Go from back
        one, two = m - 1, n - 1
        while one >= 0 and two >= 0:
            if nums2[two] > nums1[one]:
                # + 1 to adjust for 2 indices
                nums1[one + two + 1] = nums2[two]
                two -= 1
            else:
                nums1[one + two + 1] = nums1[one]
                one -= 1

        while two >= 0:
            nums1[two] = nums2[two]
            two -= 1

