# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        sum_ = 0
        len_arr = [float("inf")] * len(arr)
        res = float("inf")
        # curr_len
        left = 0
        right = 0

        while right < len(arr):
            sum_ += arr[right]

            while sum_ > target:
                sum_ -= arr[left]
                left += 1

            if sum_ == target:
                curr_len = right - left + 1

                res = min(res, curr_len + len_arr[left - 1])
                len_arr[right] = min(curr_len, len_arr[right - 1])

            else:
                len_arr[right] = len_arr[right - 1]

            right += 1

        return res if res < float("inf") else -1


if __name__ == "__main__":
    sol = Solution()
    arr = [3, 2, 2, 4, 3]
    target = 3
    sol.minSumOfLengths(arr, target)
