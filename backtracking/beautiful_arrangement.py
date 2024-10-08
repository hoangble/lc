# https://leetcode.com/problems/beautiful-arrangement/
# 526. Beautiful Arrangement
#     def countArrangement(self, n: int) -> int:
#         # backtracking then check?
#         nums = [i for i in range(1, n+1)]
#         self.cnt = 0
#         n = len(nums)
#         self.permute(1, nums, n)
#         return self.cnt

#     def permute(self, start, nums, n):
#         print(start)
#         if start == n + 1 and self.beautiful(nums):
#             self.cnt += 1

#         for i in range(start, len(nums)+1):
#             self.swap(nums, i -1, start-1)
#             print(nums)

#             if nums[i-1] % i == 0 or i % nums[i-1] == 0:
#                 print("processed", nums)
#                 self.permute(start + 1, nums, n)
#             self.swap(nums, i-1, start-1)


#     def swap(self, nums, i, j):
#         if i == j: return

#         nums[i] = nums[i] + nums[j]
#         nums[j] = nums[i] - nums[j]
#         nums[i] = nums[i] - nums[j]

#         return

#     def beautiful(self, ans):
#         for idx, n in enumerate(ans, 1):
#             if not (n % idx == 0 or idx % n == 0): return False
#         return True


class Solution:
    def countArrangement(self, n: int) -> int:
        # backtracking then check?
        nums = [i for i in range(1, n + 1)]
        self.cnt = 0

        def dfs(nums, i):
            if i == n + 1:
                self.cnt += 1
                return

            for j, num in enumerate(nums):
                if not (num % i and i % num):
                    dfs(nums[:j] + nums[j + 1 :], i + 1)

        dfs(nums, 1)
        return self.cnt


#     def countArrangement(self, n: int) -> int:

#         self.res = 0
#         nums = [i for i in range(1, n+1)]

#         def dfs(nums: list, i: int = 1):
#             if i == n+1:
#                 self.res += 1
#                 return

#             for j, num in enumerate(nums):
#                 if not(num % i and i % num):
#                     dfs(nums[:j] + nums[j+1:], i+1)

#         dfs(nums)
#         return self.res
