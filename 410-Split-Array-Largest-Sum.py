class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        ans = 0
        while l <= r:
            m = (l + r) // 2
            n_splits = self.curr_split(nums, m)

            if n_splits < k:
                r = m - 1
                ans = m

            elif n_splits > k:
                l = m + 1

            else:
                r = m - 1
                ans = m
        return ans
            
        


    def curr_split(self, nums, max_sum) -> int:
        n_split = 0
        curr_sum = 0
        for n in nums:
            if curr_sum + n <= max_sum:
                curr_sum += n
            else:
                curr_sum = n
                n_split += 1
        return n_split + 1