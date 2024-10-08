# 1423. Maximum Points You Can Obtain from Cards
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # get
        # [2,2,3,4,5,6,1]
        # prefix sum: [1, 3, 6, 10, 16, 21, 22]
        # suffix sum: [22, 21,19, 16,12,7,1]
        if len(cardPoints) == k:
            return sum(cardPoints)  # still O(n) as we call sum once

        else:
            # max_ = float("inf")
            sum_ = 0
            for i in range(len(cardPoints)):
                if i < k:
                    sum_ += cardPoints[i]
            max_ = sum_

            for i in range(k - 1, -1, -1):
                sum_ += cardPoints[i + len(cardPoints) - k] - cardPoints[i]
                max_ = max(max_, sum_)
        return max_
