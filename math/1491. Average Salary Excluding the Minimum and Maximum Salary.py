from typing import List 


class Solution:
    def average(self, salary: List[int]) -> float:
        min_ = float(inf)
        max_ = -float(inf)
        cnt = 0
        sum_ = 0

        for s in salary:
            if s > max_: max_ = s
            if s < min_: min_ = s
            cnt += 1
            sum_ += s
        # print(sum_)
        return ((sum_ - max_ - min_) / (cnt - 2))
