# 394. Decode String
# https://leetcode.com/problems/decode-string/


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans_str = ""
        for s_ in s:
            if s_ == "]":
                curr_str_ = ""
                char_ = stack.pop()
                while char_ != "[":
                    curr_str_ = char_ + curr_str_
                    char_ = stack.pop()

                if char_ == "[":
                    curr_num = ""

                while stack and stack[-1].isdigit():
                    char_ = stack.pop()
                    curr_num = char_ + curr_num

                curr_str_ = curr_str_ * int(curr_num)
                stack.append(curr_str_)
            else:
                stack.append(s_)
        return "".join(stack)


sol = Solution()
s = "3[a]2[bc]"
print(sol.decodeString(s))
