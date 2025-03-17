class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # brute force
        # pos_cnt = 0
        # neg_cnt = 0
        # for n in nums:
        #     neg_cnt += n < 0
        #     pos_cnt += n > 0
        # return max(neg_cnt, pos_cnt)
    
        # binary search for the right-most negative and the left-most positive
        # right most negative
        if len(nums) == 1:
            return 1 if nums[0] != 0 else 0

        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)

        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] < 0:
                l = m + 1
            elif nums[m] == 0:
                r = m - 1
            else:
                r = m - 1
        # now l > r
        neg_cnt = l if nums[l] < 0 else r + 1
        # print(l, r)
        # print(neg_cnt)
        if neg_cnt == n - 1:
            return neg_cnt
        
        # the left-most positive
        l = neg_cnt + 1
        r = n - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] > 0:
                r = m - 1
            elif nums[m] == 0:
                l = m + 1
            else:
                l = m + 1
        
        pos_cnt = n - r if nums[r] > 0 else n - l
        # print(l, r)
        # print(pos_cnt)
        return max(pos_cnt, neg_cnt)
