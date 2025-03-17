# class Solution:
#     def calculate(self, s: str) -> int:
#         self.i = 0
#         if len(s) == 0:
#             return 0
#         return self.cal(s + "+", 0)

#     def cal(self, s, it):
#         num = 0
#         last_num = 0
#         last_sign = "+"
#         while it < len(s):
#             if "0" <= s[it] <= "9":
#                 num = num * 10 + (ord(s[it]) - ord("0"))

#             elif s[it] in {"+", "-", "(", ")"}:
#                 if s[it] == "+" or s[it] == "-":
#                     if last_sign == "-":
#                         num = num * -1
#                     last_num += num
#                     num = 0
#                     last_sign = s[it]
#                     it += 1

#                 elif s[it] == "(":
#                     last_num = self.cal(s, it + 1)
#                     it += 1
#                 else:
#                     if last_sign == "-":
#                         num = num * -1
#                     last_num += num
#                     return last_num

#         return last_num


class Solution:
    def calculate(self, s: str) -> int:
        self.i = 0
        return self.evaluate(s + "+")

    def evaluate(self, s):
        sign = "+"
        number = 0
        ans = 0
        while self.i < len(s):
            while "0" <= s[self.i] <= "9":
                number = number * 10 + (ord(s[self.i]) - ord("0"))
                self.i += 1

            c = s[self.i]
            if c == "(":
                self.i += 1
                number = self.evaluate(s)

            if c in {"+", "-", ")"}:
                if c == "+" or c == "-":
                    if sign == "-":
                        number = number * -1
                    ans += number
                    sign = c
                    number = 0
                elif c == ")":
                    return ans

            self.i += 1
        return ans


Solution().calculate("(1+(4+5+2)-3)+(6+8)")
