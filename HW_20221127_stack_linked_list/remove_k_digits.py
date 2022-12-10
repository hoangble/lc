# 402. Remove K Digits
# https://leetcode.com/problems/remove-k-digits/description/


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num): return "0"

        stack = []

        for n_ in num:
            while stack and k and stack[-1] > n_:
                stack.pop()
                k -= 1

            if stack or n_ != "0":
                stack.append(n_)

        if k:
            stack = stack[0:-k]

        if stack:
            return "".join(stack)
        else:
            return "0"