# 2451. Odd String Difference
# https://leetcode.com/problems/odd-string-difference/ 

from typing import List
class Solution:
    def oddString(self, words: List[str]) -> str:
        self.dict_ = {chr(value + 97): value for value in range(26)}
        differences = []
        for word in words:
            w_d = self.cal_diff(word)
            differences.append(w_d)
        
        for i, diff in enumerate(differences):
            cnt = 0
            for j, diff_ in enumerate(differences):
                if diff_ == diff: cnt += 1
            if cnt ==1: return words[i]
        
    def cal_diff(self, word):
        difference = []
        for i in range(1, len(word)):
            difference.append(self.dict_[word[i]] - self.dict_[word[i-1]])
        return difference