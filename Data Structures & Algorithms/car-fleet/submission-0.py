class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # By the O(nlogn), we can see there is some kind of sort used
        # We know if the car behind gets to the target faster,
        # then they become part of the same fleet. We can use
        # a stack to represent this where we push the time it
        # takes for each car starting from the end to get to
        # the target. If the current car "collides" with the 
        # car in the top of the stack, then they form a car fleet.
        # We only keep the car with the slowest time to get
        # to the end in the stack.
        # We return the length of the stack (unique car fleets)

        pairs = [[pos, spd] for pos, spd in zip(position, speed)]
        car_fleet = [] # Stack

        for pos, spd in sorted(pairs)[::-1]: # From the end
            car_fleet.append((target - pos) / spd)

            # Check collision if at least 2 cars in car_fleet stack
            if len(car_fleet) >= 2 and car_fleet[-1] <= car_fleet[-2]:
                car_fleet.pop()

        return len(car_fleet)
