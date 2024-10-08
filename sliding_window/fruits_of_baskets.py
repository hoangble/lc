# https://leetcode.com/problems/fruit-into-baskets/submissions/
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # hash map for fruit type cnt
        fruit_type_cnt = {}
        for fruit in fruits:
            if fruit not in fruit_type_cnt:
                fruit_type_cnt[fruit] = 0

        #### sliding window
        left = 0
        right = 0
        max_cnt = 0

        cnt = 0

        # criteria: in the window, there are only 2 types of fruits
        while right < len(fruits):
            fruit_type_cnt[fruits[right]] += 1
            if fruit_type_cnt[fruits[right]] == 1:
                cnt += 1

            while cnt > 2:
                fruit_type_cnt[fruits[left]] -= 1
                if fruit_type_cnt[fruits[left]] == 0:
                    cnt -= 1
                left += 1

            max_cnt = max(max_cnt, right - left + 1)

            right += 1

        return max_cnt
