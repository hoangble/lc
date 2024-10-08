class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        ans = ""
        while n > 0:
            n -= 1
            to_convert = n % 26
            ans += chr(to_convert + 65)
            n = n - (n // 26)

        return ans


# convert from base 10 to binary for practice
def convert_to_bin(n: int) -> str:
    ans = ""
    while n > 0:
        ans = str(n % 2) + ans
        n = n // 2
    return ans


for i in range(11):
    print(i, convert_to_bin(i), bin(i))
