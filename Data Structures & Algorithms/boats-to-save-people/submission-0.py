class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        l, r = 0, len(people) - 1

        while l <= r:
            if people[r] + people[l] <= limit:
                r -= 1
                l += 1
                count += 1
            else:
                r -= 1
                count += 1
        return count