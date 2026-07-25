class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_dist = float("inf")
        res_start_idx = 0
        dist_arr = arr.copy()

        # Calculate distance to x
        for i in range(len(arr)):
            dist_arr[i] = abs(dist_arr[i] - x)
        
        for i in range(len(dist_arr) - k + 1):
            total = 0
            for j in range(k):
                total += dist_arr[i + j]

            if total < min_dist:
                min_dist = total
                res_start_idx = i

        res = []
        for i in range(k):
            res.append(arr[i + res_start_idx])
        return res


