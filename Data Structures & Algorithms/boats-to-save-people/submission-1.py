class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # O(nlogn) solution
        # people.sort()
        # count = 0
        # l, r = 0, len(people) - 1

        # while l <= r:
        #     if people[r] + people[l] <= limit:
        #         r -= 1
        #         l += 1
        #         count += 1
        #     else:
        #         r -= 1
        #         count += 1
        # return count

        count = [0] * (max(people) + 1)
        for p in people:
            count[p] += 1
        
        replace = 0
        for i, val in enumerate(count):
            while val > 0:
                people[replace] = i
                replace += 1
                val -= 1
        
        res = 0
        l, r = 0, len(people) - 1

        while l <= r:
            if people[r] + people[l] <= limit:
                r -= 1
                l += 1
                res += 1
            else:
                r -= 1
                res += 1
        return res
            
