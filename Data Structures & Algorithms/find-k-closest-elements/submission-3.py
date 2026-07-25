class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        total = 0
        
        # Load total
        for i in range(k):
            total += arr[i]

        min_dist = total
        left, right = 0, k

        for i in range(len(arr) - k):
            # Calculate "sliding window of size k" one over
            total += abs(arr[i + k] - x) - abs(arr[i] - x)

            if total < min_dist:
                min_dist = total
                left = i + 1
                right = i + 1 + k

        return arr[left:right]


