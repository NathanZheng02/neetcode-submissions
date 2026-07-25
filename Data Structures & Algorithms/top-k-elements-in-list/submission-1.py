class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = [[] for i in range(len(nums))]
        for key, val in count.items():
            freq[val - 1].append(key)
        
        res = []
        for i in range(len(nums) - 1, -1, -1):
            while k > 0 and freq[i]:
                res.append(freq[i].pop())
                k -= 1
        return res
