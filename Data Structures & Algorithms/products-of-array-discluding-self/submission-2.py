class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Easy way out: multiply all and divide by current
        # total = 1
        # zero = 0
        # for num in nums:
        #     if num != 0:
        #         total *= num
        #     else:
        #         zero += 1
        # if zero > 1:
        #     return [0] * len(nums)
        
        # res = []
        # for num in nums:
        #     if zero > 0:
        #         if num == 0:
        #             res.append(total)
        #         else:
        #             res.append(0)
        #     else:
        #         res.append(int(total / num))
        # return res

        # Now with O(n) without division?
        # Prefix/Postfix
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1 , -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res