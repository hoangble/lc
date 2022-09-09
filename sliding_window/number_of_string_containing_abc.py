# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/submissions/

from typing import List

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # find the smallest substrings containing a, b, and c
        left_ptr = 0
        right_ptr = 0 
        cnt = 0
        cnt_dict = {"a": 0, "b": 0, "c": 0}
        while right_ptr < len(s):
            cnt_dict[s[right_ptr]] += 1

            if cnt_dict["a"]*cnt_dict["b"]*cnt_dict["c"] != 0:
                # only move left when all a b c in substr
                while cnt_dict[s[left_ptr]] > 1:
                    cnt_dict[s[left_ptr]] -= 1
                    left_ptr += 1
                    
                cnt += left_ptr + 1

            # always move right
            right_ptr += 1
        return cnt