class Solution:
    def isNumber(self, s: str) -> bool:
        sign = False
        e = False
        number = False
        decimal = False
        for c in s:
            if ord("0") <= ord(c) <= ord("9"):
                number = True
                continue

            if c == "-" or c == "+":
                if sign:
                    return False
                sign = True
                continue

            if c == "e" or c == "E":
                if e or not number:
                    return False
                e = True
                continue

            if c == ".":
                if decimal or not number:
                    return False
                decimal = True
                continue

            return False
        return number

sol = Solution()
sol.isNumber(".1")