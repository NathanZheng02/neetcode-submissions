class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Using a stack to simulate asteroid destruction
        stack = []

        # If asteroids move left, they never collide. If they move right,
        # then they can collide with oncoming
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if abs(stack[-1]) < abs(a):
                    stack.pop()
                elif abs(stack[-1]) > abs(a):
                    a = 0
                    break
                else:
                    stack.pop()
                    a = 0

            if a != 0:
                stack.append(a)

        return stack

