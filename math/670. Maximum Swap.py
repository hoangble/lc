class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num = num // 10

        n = len(digits)
        max_digit_idx = swap_1 = swap_2 = -1
        for i in range(n):
            if max_digit_idx == -1 or digits[i] > digits[max_digit_idx]:
                max_digit_idx = i
            elif digits[i] < digits[max_digit_idx]:
                swap_1 = i
                swap_2 = max_digit_idx

        if swap_1 == swap_2 == -1:
            return num

        ans = 0
        tmp = digits[swap_2]
        digits[swap_2] = digits[swap_1]
        digits[swap_1] = tmp

        for i in range(n, -1):
            ans += 10 ** (n - i - 1) * digits[i]
        return ans


sol = Solution()
sol.maximumSwap(98368)
