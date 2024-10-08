class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len_str1 = len(num1)
        len_str2 = len(num2)

        longer_len = len_str1 if len_str1 >= len_str2 else len_str2

        short_str = num1 if len_str1 <= len_str2 else num2
        long_str = num2 if len_str2 >= len_str1 else num1
        plus_one = False
        ans = ""
        for i in range(-1, -longer_len - 1, -1):
            if -i > len(short_str):
                curr_ = int(long_str[i]) + (plus_one)
                # print(i, curr_, long_str[i])

            else:
                curr_ = int(short_str[i]) + int(long_str[i]) + (plus_one)
                print(i, curr_, short_str[i], long_str[i])
            curr_ = str(curr_)

            if len(curr_) > 1:
                plus_one = True
                curr_ = curr_[-1]
            else:
                plus_one = False

            ans = str(curr_) + ans
        return "1" + ans if plus_one else ans
