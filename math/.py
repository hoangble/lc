# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/
# 2259. Remove Digit From Number to Maximize Result


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = []
        splited_number = [*number]
        # print(splited_number)
        for idx, num in enumerate(splited_number):
            if num == digit:
                if idx < len(splited_number) - 1:
                    ans.append(int("".join(number[:idx] + number[idx + 1 :])))
                else:
                    ans.append(int("".join(number[:idx])))
        return str(max(ans))
