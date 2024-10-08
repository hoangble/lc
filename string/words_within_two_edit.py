# https://leetcode.com/problems/words-within-two-edits-of-dictionary/
# 2452. Words Within Two Edits of Dictionary

from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        ans_ = []
        for q in queries:
            for d in dictionary:
                if self.edit_cnt(q, d):
                    ans.append(q)
                    continue

        for w in queries:
            if w in ans:
                ans_.append(w)
        return ans_

    def edit_cnt(self, query, dict_word):
        cnt = 0
        for q, d in zip(query, dict_word):
            if q != d:
                cnt += 1
        return cnt <= 2


# %%
arr = [1, 2]

arr[0] = arr[0] + arr[1]
arr[1] = arr[0] - arr[1]
arr[0] = arr[0] - arr[1]

print(arr)
