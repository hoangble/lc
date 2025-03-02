from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # each digit can be from 0-9, each number can be at most of length 9
        max_sum_each_group = [0] * 82
        ans = -1
        for n in nums:
            digit_sum = self.cal_digit_sum(n)
            if max_sum_each_group[digit_sum] > 0:
                # this will take care of the sum between the max and the 2nd max
                ans = max(ans, max_sum_each_group[digit_sum] + n)
            # just need to store the current max of this group
            max_sum_each_group[digit_sum] = max(max_sum_each_group[digit_sum], n)
        return ans

    def cal_digit_sum(self, num):
        ans = 0
        while num > 0:
            ans += num % 10
            num = num // 10
        return ans


nums = [
    229,
    398,
    269,
    317,
    420,
    464,
    491,
    218,
    439,
    153,
    482,
    169,
    411,
    93,
    147,
    50,
    347,
    210,
    251,
    366,
    401,
]
Solution().maximumSum(nums)
