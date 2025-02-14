class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # split before and after the '.'
        dec_idx1 = -1
        if \.\ in num1:
            for i in range(len(num1)):
                if num1[i] == \.\:
                    dec_idx1 = i
                    break

        dec_idx2 = -1
        if \.\ in num2:
            for j in range(len(num2)):
                if num2[j] == \.\:
                    dec_idx2 = j
                    break

        carry = 0
        to_add_dec = False
        # neg1 = True if num1[0] == \-\ else False
        # neg2 = True if num2[0] == \-\ else False
        if dec_idx1 != -1 and dec_idx2 != -1:
            dec1 = num1[dec_idx1 + 1 :]
            dec2 = num2[dec_idx2 + 1 :]
            if len(dec1) > len(dec2):
                dec2 = dec2 + \0\ * (len(dec1) - len(dec2))
            elif len(num1[dec_idx1 + 1 :]) < len(dec2):
                dec1 = dec1 + \0\ * (len(dec2) - len(dec1))

            after_dec, carry = self.add_(dec1, dec2, 0)
            before_dec, carry = self.add_(num1[:dec_idx1], num2[:dec_idx2], carry)
            to_add_dec = True

        elif dec_idx1 == -1 and dec_idx2 == -1:
            after_dec = []
            before_dec, carry = self.add_(num1, num2, carry)

        elif dec_idx1 == -1:
            after_dec = [*num2[dec_idx2 + 1 :]][::-1]
            before_dec, carry = self.add_(num1, num2[:dec_idx2], carry)
            to_add_dec = True

        else:
            after_dec = [*num1[dec_idx1 + 1 :]][::-1]
            before_dec, carry = self.add_(num1[:dec_idx1], num2, carry)
            to_add_dec = True

        after_dec_str = [str(i) for i in after_dec[::-1]]

        if carry:
            before_dec.append(carry)

        before_dec_str = [str(i) for i in before_dec[::-1]]
        if to_add_dec:
            before_dec_str.append(\.\)
        return \\.join(before_dec_str + after_dec_str)
    
    def add_(self, s1: str, s2: str, carry: int) -> Tuple[List[str], int]:
        i = len(s1) - 1
        j = len(s2) - 1

        ans = []
        while i >= 0 or j >= 0:
            c1 = ord(s1[i]) - ord(\0\) if i >= 0 else 0
            c2 = ord(s2[j]) - ord(\0\) if j >= 0 else 0
            curr = (c1 + c2 + carry) % 10
            carry = (c1 + c2 + carry) // 10
            ans.append(curr)
            i -= 1
            j -= 1

        return ans, carry

        