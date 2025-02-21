from collections import deque
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dq = deque([(0, 0)])
        visited = set()
        visited.add((0, 0))

        ans = []

        while dq:
            x, y = dq.popleft()
            print(x, y)
            ans.append(nums[x][y])

            if x + 1 < len(nums) and (x + 1, y) not in visited:
                dq.append((x + 1, y))
                visited.add((x + 1, y))

            if y + 1 < len(nums[x]) and (x, y + 1) not in visited:
                dq.append((x, y + 1))
                visited.add((x, y + 1))

        return ans


Solution().findDiagonalOrder([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]])
