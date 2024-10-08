# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/
# 2260. Minimum Consecutive Cards to Pick Up

from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_index = dict()
        min_dict = dict()
        for idx, num in enumerate(cards):
            if num not in min_dict:
                min_dict[num] = len(cards) + 1
            else:
                min_dict[num] = min(idx - last_index[num] + 1, min_dict[num])
            last_index[num] = idx

        min_card = min(min_dict.values())
        return min_card if min_card <= len(cards) else -1
