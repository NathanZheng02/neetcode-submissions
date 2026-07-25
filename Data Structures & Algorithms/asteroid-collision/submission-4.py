class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Using a stack to simulate asteroid destruction
        stack = []

        # Only collide if stack has one right and incoming is left
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                # Destroy stack asteroid
                if abs(stack[-1]) < abs(a):
                    stack.pop()
                # Current asteroid is destroyed
                elif abs(stack[-1]) > abs(a):
                    a = 0
                    break
                # Both destroyed
                else:
                    a = 0
                    stack.pop()

            if a != 0:
                stack.append(a)

        return stack

