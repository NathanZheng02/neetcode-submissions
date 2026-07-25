from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Use 2 pointer for finding j and k
        # Iterate through all possible values of i
        res = []
        nums.sort() # O(nlog(n))

        for i in range(len(nums) - 1):
            # Check to see if nums[i] is already used
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                target = -nums[i]
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                
                    # Remove duplicates for left + right pointers by shifting left
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res
        