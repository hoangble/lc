# class Solution:
#     def calculate(self, s: str) -> int:
#         last_sign = "+"
#         ans = 0
#         curr = 0
#         last = 0
#         s = s + "+"

#         i = 0
#         while i < len(s):
#             while "0" <= s[i] <= "9":
#                 curr = curr * 10 + (ord(s[i]) - ord("0"))
#                 i += 1

#             c = s[i]
#             if c in {"+", "-", "*", "/"}:
#                 if last_sign == "+" or last_sign == "-":
#                     ans += last
#                     last = curr if last_sign == "+" else curr * -1
#                 elif last_sign == "*":
#                     last = last * curr
#                 elif last_sign == "/":
#                     last = int(last / curr)

#                 curr = 0
#                 last_sign = c
#             i += 1
#         ans += last
#         return ans


class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        n = len(s)
        last_sign = "+"
        last_num = 0
        s = s + "+"

        num = 0
        ans = 0
        i = 0
        while i < n:
            while "0" <= s[i] <= "9":
                num = num * 10 + (ord(s[i]) - ord("0"))
                i += 1

            c = s[i]
            if c in {"+", "-", "/", "*"}:
                if last_sign == "+" or last_sign == "-":
                    ans += last_num
                    last_num = num if last_sign == "+" else num * -1
                elif last_sign == "*":
                    last_num = num * last_num
                else:
                    last_num = int(last_num / num)
                last_sign = c
                num = 0
            i += 1
        ans += last_num
        return ans


sol = Solution().calculate(" 3/2 ")
