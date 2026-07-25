class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # At most 2 results
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            # At most 2 results for floor(n / 3)
            if len(count) < 3:
                continue
            
            # Decrement by 1 and pop elements with 0 counts
            new_count = defaultdict(int)
            for n, c in count.items():
                if c > 1:
                    new_count[n] = c - 1
            count = new_count

        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res
            