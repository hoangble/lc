# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/ 
# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap_char_cnt = {}
        for i in set(s):
            hashmap_char_cnt[i] = 0
        
        left = 0
        right = 0
        longest_cnt = 0
        
        for right in range(len(s)):
            hashmap_char_cnt[s[right]] += 1
            
            while not self.check_if_valid(hashmap_char_cnt):
            # while hashmap_char_cnt[s[right]] > 1:

                hashmap_char_cnt[s[left]] -= 1
                left += 1
        
            longest_cnt = max(longest_cnt, right - left + 1)

        return longest_cnt
                
    def check_if_valid(self, hashmap_unique_cnt):
        for val in hashmap_unique_cnt.values():
            if val > 1:
                return False
        return True
    