class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        ops = {"+", "-", "*", "/"}
        last_ops = "+"
        ans = 0
        curr_num = 0
        for i, c in enumerate(s):
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)

            if c in ops or i == len(s) - 1:  # see operator
                match last_ops:
                    case "+":
                        stack.append(curr_num)
                    case "-":
                        stack.append(-1 * curr_num)
                    case "*" | "/":
                        stack.append(self.do_ops(last_ops, stack.pop(), curr_num))

                curr_num = 0
                last_ops = c

        while stack:
            ans += stack.pop(0)
        return ans
    
    def do_ops(self, op: str, a: int, b: int) -> int:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a // b


sol = Solution()
print(sol.calculate("14-3/2"))
