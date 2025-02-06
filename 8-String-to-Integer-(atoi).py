class Solution:
    def myAtoi(self, s: str) -> int:
        ans = []

        number = False
        negative = False
        for s_ in s:
            if number: 
                if not s_.isnumeric():
                    break
                ans.append(s_)
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
                        ans.append(s_)
                else:
                    break
        
        ans_num = 0
        for i in range(len(ans)):
            ans_num += int(ans[i]) * 10 ** (len(ans) - i - 1)
        
        ans = ans_num if not negative else -ans_num
        # rounding
        if ans < 0:
            MIN = -2 ** 31
            ans = max(ans, MIN)
        else:
            MAX = 2 ** 31 - 1
            ans = min(ans, MAX)
        return ans
            