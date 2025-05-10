class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_string = []
        for c in s:
            if c == "[":
                stack.append(''.join(curr_string))
                stack.append(curr_num)
                curr_string = []
                curr_num = 0
            elif c == "]":
                num = stack.pop()
                prev_string = stack.pop()
                if prev_string != '':
                    curr_string = [prev_string] + num * curr_string
                else:
                    curr_string = num * curr_string

            elif "0" <= c <= "9":
                curr_num = curr_num * 10 + (ord(c) - ord("0"))
            else:
                curr_string.append(c)
        return "".join(curr_string)


Solution().decodeString("3[a]2[bc]")
