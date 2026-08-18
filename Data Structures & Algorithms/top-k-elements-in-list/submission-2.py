class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = [[] for _ in range(len(nums) + 1)]
        for key, val in count.items():
            freq[val].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for c in freq[i]:
                res.append(c)
                if len(res) == k:
                    return res
