# variant where there are signs and decimal numbers
from typing import List, Tuple


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # split before and after the '.'

        carry = 0
        to_add_dec = False
        if num1[0] == "-":
            neg1 = -1
            num1 = num1[1:]
        else:
            neg1 = 1

        if num2[0] == "-":
            neg2 = -1
            num2 = num2[1:]
        else:
            neg2 = 1

        dec_idx1 = self.get_dec_idx(num1)
        dec_idx2 = self.get_dec_idx(num2)
        # preprocess
        if dec_idx1 != -1 and dec_idx2 != -1:
            dec1 = num1[dec_idx1 + 1 :]
            dec2 = num2[dec_idx2 + 1 :]
            if len(dec1) > len(dec2):
                dec2 = dec2 + "0" * (len(dec1) - len(dec2))
            elif len(num1[dec_idx1 + 1 :]) < len(dec2):
                dec1 = dec1 + "0" * (len(dec2) - len(dec1))

            after_dec, carry = self.add_(dec1, dec2, 0, neg1, neg1)
            before_dec, carry = self.add_(num1[:dec_idx1], num2[:dec_idx2], carry, neg1, neg2)
            to_add_dec = True

        elif dec_idx1 == -1 and dec_idx2 == -1:
            after_dec = []
            before_dec, carry = self.add_(num1, num2, carry, neg1, neg2)

        elif dec_idx1 == -1:
            after_dec = [*num2[dec_idx2 + 1 :]][::-1]
            before_dec, carry = self.add_(num1, num2[:dec_idx2], carry, neg1, neg2)
            to_add_dec = True

        else:
            after_dec = [*num1[dec_idx1 + 1 :]][::-1]
            before_dec, carry = self.add_(num1[:dec_idx1], num2, carry, neg1, neg2)
            to_add_dec = True

        after_dec_str = [str(i) for i in after_dec[::-1]]

        if carry:
            before_dec.append(carry)

        before_dec_str = [str(i) for i in before_dec[::-1]]
        if to_add_dec:
            before_dec_str.append(".")
        return "".join(before_dec_str + after_dec_str)

    def get_dec_idx(self, s) -> int:
        dec_idx = -1
        if "." in s:
            for i in range(len(s)):
                if s[i] == ".":
                    dec_idx = i
                    break
        return dec_idx

    def add_(
        self, s1: str, s2: str, carry: int, s1_neg: int = 1, s2_neg: int = 1
    ) -> Tuple[List[str], int]:
        i = len(s1) - 1
        j = len(s2) - 1

        ans = []
        while i >= 0 or j >= 0:
            c1 = (ord(s1[i]) - ord("0")) * s1_neg if i >= 0 else 0
            c2 = (ord(s2[j]) - ord("0")) * s2_neg if j >= 0 else 0
            if s2_neg < s1_neg and abs(c1) < abs(c2) + abs(carry):
                c1 = c1 + 1
                curr = (c1 + c2 + carry) % 10
                carry = -1
            else:
                curr = (c1 + c2 + carry) % 10
                carry = (c1 + c2 + carry) // 10
            ans.append(curr)
            i -= 1
            j -= 1

        return ans, carry

    def compare(self, s1, s2):
        if len(s1) > len(s2):
            return 1

        if len(s1) < len(s2):
            return -1

        if len(s1) == 0:
            return 0

        i = 0

        while i < len(s1):
            c1 = ord(s1[i]) - ord("0")
            c2 = ord(s2[i]) - ord("0")
            if c1 > c2:
                return 1
            elif c1 < c2:
                return -1
            i += 1

        return 0


if __name__ == "__main__":
    # assert Solution().addStrings("0.6", "0.28") == "0.88"
    # assert Solution().addStrings("0.6", "0.2") == "0.8"

    # assert Solution().addStrings("6", "0.28") == "6.28"
    # assert Solution().addStrings("6", "-0.28") == "5.72"

    # assert Solution().addStrings("0.7", "-0.2") == "0.5"
    # assert Solution().addStrings("100", "12") == "112"
    assert Solution().addStrings("-1", "22") == "21"
