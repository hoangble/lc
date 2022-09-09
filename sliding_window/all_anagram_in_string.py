# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # p can be aab
        if len(p) > len(s):
            return []
        ans = []
        # anagram
        p_dict = {}
        s_dict = {}
        for c in range(26):
            curr = chr(ord('a') + c)
            p_dict[curr] = 0
            s_dict[curr] = 0 

        for c in p:
            p_dict[c] += 1
       
        ### init for first window
        for i in range(len(p)):
            s_dict[s[i]] += 1
            
        if self.check_anagram(s_dict, p_dict):
            ans.append(0)
        
        ###
        for right in range(len(p), len(s)): # s = "a"
            left = right - len(p) + 1
            s_dict[s[left-1]] -= 1
            s_dict[s[right]] += 1
            if self.check_anagram(s_dict, p_dict):
                ans.append(left)
        
        return ans
            
    def check_anagram(self, s_dict, p_dict):
        for c, cnt in s_dict.items():
            if cnt != p_dict[c]:
                return False
        return True