class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_delete = set()
        stack = []
        for i, s_ in enumerate(s):
            if s_ == "(":
                stack.append(i)
            elif s_ == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    to_delete.add(i)

        to_delete = to_delete.union(set(stack))
        ans = []
        for i, s_ in enumerate(s):
            if i not in to_delete:
                ans.append(s_)
        return "".join(ans)
