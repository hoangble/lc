# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_cnt = 0
        left_ptr = 0
        right_ptr = 0
        vowel_cnt = 0
        vowels_list = ["a", "e", "i", "o", "u"]

        # loop through all substring of size k
        while right_ptr < len(s):
            if s[right_ptr] in vowels_list:
                vowel_cnt += 1
            while right_ptr - left_ptr + 1 > k:
                if s[left_ptr] in vowels_list:
                    vowel_cnt -= 1
                left_ptr += 1
            max_cnt = max(max_cnt, vowel_cnt)
            right_ptr += 1
        return max_cnt
