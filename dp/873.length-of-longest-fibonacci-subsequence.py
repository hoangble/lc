from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        ans = 0

        for curr in range(2, n):
            start = 0
            end = curr - 1
            while start < end:
                curr_sum = arr[start] + arr[end]
                if curr_sum > arr[curr]:
                    end -= 1
                elif curr_sum < arr[curr]:
                    start += 1
                else:
                    dp[end][curr] = dp[start][end] + 1
                    ans = max(ans, dp[end][curr])
                    end -= 1
                    start += 1
        return ans + 2 if ans > 0 else 0
