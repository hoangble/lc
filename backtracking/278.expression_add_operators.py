from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # backtrack
        n = len(num)
        ans = []

        def recurse(idx, prev_op, curr_op, val, s):
            if idx == n:
                if val == target and curr_op == 0:
                    ans.append("".join(s[1:]))
                return

            curr_op = curr_op * 10 + int(num[idx])
            str_op = str(curr_op)

            # to avoid 1 + 05
            if curr_op > 0:
                recurse(idx + 1, prev_op, curr_op, val, s)

            # addition
            s.append("+")
            s.append(str_op)
            recurse(idx + 1, curr_op, 0, val + curr_op, s)
            s.pop()
            s.pop()

            if s:
                s.append("-")
                s.append(str_op)
                recurse(idx + 1, -curr_op, 0, val - curr_op, s)
                s.pop()
                s.pop()

                s.append("*")
                s.append(str_op)
                recurse(idx + 1, curr_op * prev_op, 0, val - prev_op + (curr_op * prev_op), s)
                s.pop()
                s.pop()

        recurse(0, 0, 0, 0, [])
        return ans


Solution().addOperators("123", "6")
