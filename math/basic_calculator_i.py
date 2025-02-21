class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0

        stack = []

        sign = 1
        ans = curr = 0
        for i, c in enumerate(s):
            if self.is_num(c):
                curr = curr * 10 + (ord(c) - ord("0"))
            elif c == "+" or c == "-":
                ans += curr * sign
                curr = 0
                sign = 1 if c == "+" else -1
                if stack:
                    sign = sign * stack[-1]
            elif c == "(":
                stack.append(sign)
            elif c == ")":
                stack.pop()
        ans = sign * curr
        return ans

    def is_num(self, c):
        return "0" <= c <= "9"


Solution().calculate(" 2-1 + 2 ")
