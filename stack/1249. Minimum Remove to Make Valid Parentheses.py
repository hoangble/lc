# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         to_delete = set()
#         stack = []
#         for i, s_ in enumerate(s):
#             if s_ == "(":
#                 stack.append(i)
#             elif s_ == ")":
#                 if len(stack) > 0:
#                     stack.pop()
#                 else:
#                     to_delete.add(i)

#         to_delete = to_delete.union(set(stack))
#         ans = []
#         for i, s_ in enumerate(s):
#             if i not in to_delete:
#                 ans.append(s_)
#         return "".join(ans)


# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         # no stack
#         open_cnt = 0
#         arr = [*s]

#         for i, c in enumerate(arr):
#             if c == "(":
#                 open_cnt += 1
#             elif c == ")":
#                 if open_cnt > 0:
#                     open_cnt -= 1
#                 else:
#                     arr[i] = "*"

#         for i in range(len(arr) - 1, -1, -1):
#             if open_cnt > 0 and arr[i] == "(":
#                 open_cnt -= 1
#                 arr[i] = "*"

#         return "".join(c for c in arr if c != "*")


# Solution().minRemoveToMakeValid("))((")


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        close = 0
        for c in s:
            if c == ")":
                close += 1

        n = len(s)
        curr_open = curr_close = 0
        ans = []
        for c in s:
            if c != "(" and c != ")":
                ans.append(c)
                continue

            if c == "(":
                if curr_open < close:
                    ans.append(c)
                    curr_open += 1
            else:
                if curr_open == curr_close:
                    close -= 1
                else:
                    curr_close += 1
                    ans.append(c)
        return "".join(ans)


Solution().minRemoveToMakeValid("))((")
