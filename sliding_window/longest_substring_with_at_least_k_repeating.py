class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import Counter, defaultdict
        
        max_len = 0
        for max_allowed_unique_chars in range(1, len(Counter(s))+1):
            left = 0
            right = 0
            
            current_unique_chars = 0
            freq_count_greater_or_equal_k = 0
            
            freq_count = defaultdict(int)
            while right < len(s):
                freq_count[s[right]] += 1
                if freq_count[s[right]] == 1: current_unique_chars += 1
                if freq_count[s[right]] == k: freq_count_greater_or_equal_k += 1
                
                while current_unique_chars > max_allowed_unique_chars:
                    if freq_count[s[left]] == 1: current_unique_chars -= 1
                    if freq_count[s[left]] == k: freq_count_greater_or_equal_k -= 1
                    freq_count[s[left]] -= 1
                    left += 1
                    
                if self.check_valid(k, freq_count):
                    max_len = max(max_len, right - left +1)

                right += 1
        return max_len
    
    def check_valid(self, k, freq_cnt_dict):
        for char_, cnt_ in freq_cnt_dict.items():
            if cnt_ > 0 and cnt_ < k:
                return False
        return True
                
                