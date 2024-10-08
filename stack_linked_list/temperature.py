from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1][0]]:
                prev_day, _ = stack.pop()
                ans[prev_day] = i - prev_day
            stack.append((i, temperatures[i]))
        return ans


t = [73, 74, 75, 71, 69, 72, 76, 73]
sol = Solution()
sol.dailyTemperatures(t)

# %%
import numpy as np


def powerup(i):
    if i == 1:
        return 1
    return np.square(i) + powerup(i - 1)


powerup(4)


# %%
def great(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return max(a, b)


great(21, 35)

# %%
j = 1
k = 2
for i in range(3):
    j += k
    k += j
print(1)
