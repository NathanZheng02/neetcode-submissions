class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            # Merging by taking 2 subarrays and overwrite nums
            left, right = arr[l : m + 1], arr[m + 1 : r + 1]

            # i: pointer for main array (nums)
            # j: pointer for left subarray
            # k: pointer for right subarray
            i, j, k = l, 0, 0
            while j < len(left) and k < len(right):
                # Sorting by smallest
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            # Case: One of the subarrays is done
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1
        
        def mergeSort(arr, l, r):
            # Base Case
            if l == r:
                return
            
            # Dividing into 2 halves recursively
            m = l + (r - l) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)

            # Merging left and right sides
            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums))
        return nums