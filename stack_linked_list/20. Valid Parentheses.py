class Solution:
    from collections import deque

    def isValid(self, s: str) -> bool:
        stack = deque([])

        for s_ in s:
            if s_ == ")":
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if p != "(":
                    return False
            elif s_ == "]":
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if p != "[":
                    return False
            elif s_ == "}":
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if p != "{":
                    return False
            else:
                stack.append(s_)
            # print(stack)
        return len(stack) == 0

    # cleaner code
    def isValid(self, s: str) -> bool:
        stack = []
        d = {")": "(", "}": "{", "]": "["}
        for s_ in s:
            if s_ in d:
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if p != d[s_]:
                    return False
            else:
                stack.append(s_)
        return len(stack) == 0
