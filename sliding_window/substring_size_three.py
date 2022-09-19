# 1876. Substrings of Size Three with Distinct Characters 
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = 0
        right = 0
        cnt = 0
        hashmap = {}
        for s_ in set(s):
            hashmap[s_] = 0
        
        while right < len(s):
            hashmap[s[right]] += 1
            
            while right - left + 1 > 3:
                hashmap[s[left]] -= 1
                left += 1
            cnt += self.checkGoodString(hashmap)
                
            right += 1
            # print(hashmap)
        return cnt
    
    def checkGoodString(self, hashmap) -> bool:
        total_cnt = 0
        for k, v in hashmap.items():
            total_cnt += v
            if total_cnt > 3 or v > 1:
                return False
        return total_cnt == 3
        