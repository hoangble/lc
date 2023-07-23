from collections import deque
from typing import List 

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque([])

        for a in asteroids:
            if not stack:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 > a:
                    if abs(stack[-1]) < abs(a):
                        stack.pop()
                        continue
                    elif abs(stack[-1]) == abs(a):
                        stack.pop()
                    break        
                    
                else:
                    stack.append(a)
        return list(stack)
    
if __name__ == "__main__":
    asteroids = [10,2,-5]
    sol = Solution()
    sol.asteroidCollision(asteroids)

        