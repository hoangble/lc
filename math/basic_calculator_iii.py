class Solution:
    def calculate(self, s: str) -> int:
        self.i = 0
        s = s + "+"
        return self._evaluate(s)

    def _evaluate(self, s):
        num = 0
        last_num = 0
        ans = 0
        sign = "+"
        while self.i < len(s):
            while "0" <= s[self.i] <= "9":
                num = num * 10 + (ord(s[self.i]) - ord("0"))
                self.i += 1

            c = s[self.i]
            if c == "(":
                self.i += 1
                num = self._evaluate(s)

            elif c in {"+", "-", "*", "/", ")"}:
                if sign == "+" or sign == "-":
                    ans += last_num
                    last_num = num if sign == "+" else num * -1
                elif sign == "*":
                    last_num = last_num * num
                elif sign == "/":
                    last_num = int(last_num / num)

                if c == ")":
                    break
                num = 0
                sign = c
            self.i += 1
        ans += last_num
        return ans


Solution().calculate("2*(5+5*2)/3+(6/2+8)")
