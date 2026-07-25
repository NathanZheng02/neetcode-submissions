class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        gas_left = 0
        res = 0
        for i in range(len(gas)):
            gas_left += gas[i] - cost[i]

            # If the ith station is not reachable,
            # then we shift valid starting to i + 1.
            # This works because there is only 1 valid solution,
            # so it only loops when cost goes negative (i is in the
            # future values)
            if gas_left < 0:
                gas_left = 0
                res = i + 1

        return res