# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        sum_ = 0
        val_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        skip = False
        for i in range(len(s) - 1, -1, -1):
            if skip:
                skip = False
                continue
            if i != 0:
                if s[i - 1] == "I" and (s[i] == "V" or s[i] == "X"):
                    val = val_map[s[i]] - 1
                    skip = True
                elif s[i - 1] == "X" and (s[i] == "L" or s[i] == "C"):
                    val = val_map[s[i]] - 10
                    skip = True

                elif s[i - 1] == "C" and (s[i] == "D" or s[i] == "M"):
                    val = val_map[s[i]] - 100
                    skip = True

                else:
                    val = val_map[s[i]]
            else:
                val = val_map[s[i]]
            print(s[i], val)
            sum_ += val
        return sum_
