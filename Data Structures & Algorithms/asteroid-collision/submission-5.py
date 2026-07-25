class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Stackless pointer simulation - essentially copies surviving
        # asteroids into pointer slot for stack
        # Time complexity: O(n), Space complexity: O(1)
        i = -1

        # Only collide if stack has one right and incoming is left
        for a in asteroids:
            while i >= 0 and asteroids[i] > 0 and a < 0:
                # Destroy stack asteroid
                if asteroids[i] < abs(a):
                    i -= 1
                # Current asteroid is destroyed
                elif asteroids[i] > abs(a):
                    a = 0
                    break
                # Both destroyed
                else:
                    a = 0
                    i -= 1
                    break

            # If asteroid is not destroyed, we account in the pointer
            if a != 0:
                i += 1
                asteroids[i] = a

        return asteroids[:i + 1]

