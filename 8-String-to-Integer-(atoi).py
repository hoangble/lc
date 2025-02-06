class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0

        number = False
        negative = False
        MIN = -2 ** 31
        MAX = 2 ** 31 - 1

        for i, s_ in enumerate(s):
            if number: 
                if ord('0') > ord(s_) or ord(s_) >  ord('9'):
                    break
                if ans > MAX // 10 or (ans == MAX // 10 and int(s_) > MAX % 10):
                    return MAX if not negative else MIN
                ans = ans * 10 + int(s_)

            else:
                if s_ == \ \:
                    continue
                elif s_ == '-':
                    negative = True
                    number = True
                elif s_ == \+\:
                    negative = False
                    number = True
                elif ord('0') <= ord(s_) <= ord('9'):
                    number = True
                    if s_ != '0':
                        ans = ans * 10 + int(s_)
                else:
                    break
        return ans if not negative else -ans