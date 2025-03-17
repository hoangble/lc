from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        consonant_cnt = 0

        ans = 0  # cnt of strings
        vowels = {"a", "e", "i", "o", "u"}

        curr_vowels = set()
        vowel_freq = defaultdict(int)

        l = 0
        for r in range(len(word)):
            if word[r] in vowels:
                vowel_freq[word[r]] += 1
                curr_vowels.add(word[r])
            else:
                consonant_cnt += 1

            while consonant_cnt > k:
                if word[l] not in vowels:
                    consonant_cnt -= 1
                else:
                    vowel_freq[word[l]] -= 1
                    if vowel_freq[word[l]] == 0:
                        curr_vowels.remove(word[l])
                l += 1

            if consonant_cnt == k and len(curr_vowels) == 5:
                ans += 1
        return ans


Solution().countOfSubstrings("iqeaouqi", 2)
