from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        high, low = max([y + l for _, y, l in squares]), min([y for _, y, _ in squares])

        while low <= high:
            mid = (low + high) / 2
            upper, lower = self.cal_area(squares, mid)
            if upper == lower:
                return mid
            elif upper > lower:
                low = mid
            else:
                high = mid

    def cal_area(self, squares, line):
        upper = 0
        lower = 0

        for x, y, l in squares:
            if y + l <= line:
                lower += l * l
            elif y >= line:
                upper += l * l
            else:
                upper += l * (y + l - line)
                lower += l * (line - y)

        return upper, lower


Solution().separateSquares([[23, 29, 3], [28, 29, 4]])
