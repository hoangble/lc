from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans = 0

        for _, v in c.items():
            if v == 1:
                return -1
            ### or just do ceil(v / 3)
            if v % 3 == 0:
                ans += v // 3
            elif v % 3 == 2:
                ans += v // 3 + 1
            else:
                div_3_all = v // 3
                div_3 = (div_3_all - 1) + (v - ((div_3_all - 1) * 3)) // 2
                if v % 2 == 0:
                    div_2 = v // 2

                    if div_3 == 0:
                        ans += div_2
                    else:
                        ans += min(div_3, div_2)
                else:
                    ans += div_3
        return ans


if __name__ == "__main__":
    nums = [14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12]
    sol = Solution()
    sol.minOperations(nums)
