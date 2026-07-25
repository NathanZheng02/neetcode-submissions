class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This looks like a heap, but that happens with O(klog(n))
        # time, but if there is a way to solve it like a hashmap
        # while keeping track of which value is bigger, then
        # that will be more efficient.

        # HashMap to keep track of count of each unique number
        hm = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
        for key, val in hm.items():
            # key represents the unique number
            # val represents the count
            freq[val].append(key)
        ans = []
        # O(n + k) because the outer loop is running n times
        # and the inner loop is running a total of k times
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
