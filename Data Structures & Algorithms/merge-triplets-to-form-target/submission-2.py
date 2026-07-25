class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [0, 0, 0]

        for trip in triplets:
            print("Current: ", curr)
            a, b, c = trip
            
            if a <= target[0] and b <= target[1] and c <= target[2]:
                curr = [max(a, curr[0]), max(b, curr[1]), max(c, curr[2])]
        
        return curr == target
