class Solution:
    def minAddToMakeValid(self, input_string: str) -> int:
        cnt = 0
        stack_size = 0

        for s in input_string:
            if s == "(":
                stack_size += 1
            else:
                if stack_size > 0:
                    stack_size -= 1
                else:
                    cnt += 1
        return cnt + stack_size


sol = Solution()
sol.minAddToMakeValid("())")
