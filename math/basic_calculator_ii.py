class Solution:
    def calculate(self, s: str) -> int:
    
        n = len(s)
        sign = "+"
        ans = last = curr = 0
        for i, c in enumerate(s):
            if self.is_numeric(c):
                curr = (curr * 10) + (ord(c) - ord("0"))

            if (not self.is_numeric(c) and c != " ") or i == n - 1:
                if sign == "+" or sign == "-":
                    ans += last
                    last = curr if sign == "+" else -curr

                elif sign == "*":
                    last = last * curr
                elif sign == "/":
                    last = abs(last) // abs(curr)
                    if last // curr < 0:
                        last = last * -1

                curr = 0
                sign = c

        ans += last
        return ans

    def is_numeric(self, c):
        return ord("0") <= ord(c) <= ord("9")


sol = Solution().calculate("14-3/2")
